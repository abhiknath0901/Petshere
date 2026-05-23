from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model, authenticate
from .models import Pet , Cart, Order, OrderItem, Address
from .serializers import PetSerializer, CartSerializer
import razorpay
from django.conf import settings
User = get_user_model()

# Signup
@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):
    email = request.data.get('email')
    name = request.data.get('name')
    phone = request.data.get('phone')
    password = request.data.get('password')

    if not email or not name or not password:
        return Response({'error': 'Email, name, and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(email=email).exists():
        return Response({'error': 'A user with this email already exists.'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(email=email, name=name, phone=phone, password=password)
    return Response({'message': 'User created successfully.'}, status=status.HTTP_201_CREATED)

# Login
@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(request, email=email, password=password)
    if user is None:
        return Response({'error':'Invalid credentials'}, status= status.HTTP_401_UNAUTHORIZED)

    refresh = RefreshToken.for_user(user)
    return Response({
        'user':{
            'id': user.id,
            'email': user.email,
            'name': user.name,
        },
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }, status=status.HTTP_200_OK)

# Logout
@api_view(['POST'])
@permission_classes([AllowAny])
def logout_user(request):
    try:
        refresh_token = request.data.get('refresh')
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({'message': 'User logged out successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': 'Invalid token.'}, status=status.HTTP_400_BAD_REQUEST)

# Get all pets
@api_view(['GET'])
@permission_classes([AllowAny])
def get_pets(request):
    pets = Pet.objects.all()
    serializer = PetSerializer(pets, many=True)
    return Response(serializer.data)

# Get cart items for a user
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_cart(request):
    user_id = request.user.id
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

    cart_items = Cart.objects.filter(user=user)
    serializer = CartSerializer(cart_items, many=True)
    return Response(serializer.data)

# Syncing cart data from frontend to backend
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def sync_cart(request):
    user = request.user
    cart_data = request.data.get('cart',[])
    Cart.objects.filter(user=user).delete()

    for item in cart_data:
        pet_id = item.get('id')
        quantity = item.get('qty')

        if not pet_id:
                continue
        
        try:
            

            pet = Pet.objects.get(id = pet_id )
            Cart.objects.create(
                user = user,
                pet = pet,
                quantity = quantity
            )
        except Pet.DoesNotExist:
            continue
    
    return Response({
        'message' : 'Cart synced successfully.'
    })

@api_view(["POST"])
@permission_classes([IsAuthenticated])

def save_address(request):

    try:

        address = Address.objects.create(

            user=request.user,
            receiver_name = request.data.get("receiver_name"),

            receiver_phone=request.data.get("receiver_phone"),

            pincode = request.data.get("pincode"),

            house_no_or_name = request.data.get("house_no_or_name"),

            street_area_locality = request.data.get("street_area_locality"),

            city = request.data.get("city"),

            state= request.data.get("state"),

            landmark= request.data.get("landmark")
        )

        return Response({
            "message":
                "Address saved successfully",
            "address_id":
                address.id,
            "receiver_name":
                address.receiver_name,
            "city":
                address.city
        }, status= status.HTTP_201_CREATED)

    except Exception as e:
        return Response({
            "error": str(e)
        }, status= status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_payment(request):

    client = razorpay.Client(
        auth=(
            settings.RAZORPAY_KEY_ID,
            settings.RAZORPAY_KEY_SECRET
        )
    )

    cart = request.data.get("cart", [])

    total = 0

    for item in cart:

        pet = Pet.objects.get(
            id=item["id"]
        )

        total += (
            pet.price * item["qty"]
        )

    payment = client.order.create({

        "amount": total * 100,

        "currency": "INR",

        "payment_capture": 1
    })

    return Response({

        "payment": payment,

        "key":
        settings.RAZORPAY_KEY_ID
    })

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def confirm_order(request):

    cart = request.data.get("cart")

    address_id = request.data.get("address_id")

    address = Address.objects.get(
        id=address_id
    )

    total = 0

    for item in cart:

        total += item["price"] * item["qty"]

    order = Order.objects.create(

    user=request.user,

    address=address,

    total_price=total,

    payment_method="card",

    payment_status="paid",

    status="confirmed",

    razorpay_order_id=
        request.data.get(
            "razorpay_order_id"
        ),

    razorpay_payment_id=
        request.data.get(
            "razorpay_payment_id"
        )
)

    for item in cart:

        pet = Pet.objects.get(
            id=item["id"]
        )

        OrderItem.objects.create(

            order=order,

            pet=pet,

            quantity=item["qty"],

            price=item["price"]
        )

    Cart.objects.filter(
        user=request.user
    ).delete()

    return Response({

        "message":
            "Order confirmed"
    })