from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model, authenticate
from .models import Pet , Cart, Order
from .serializers import PetSerializer, CartSerializer, OrderSerializer
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

# logout
@api_view(['POST'])
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
def get_cart(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

    cart_items = Cart.objects.filter(user=user)
    serializer = CartSerializer(cart_items, many=True)
    return Response(serializer.data)

# Add to cart
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request, user_id, pet_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

    try:
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        return Response({'error': 'Pet not found.'}, status=status.HTTP_404_NOT_FOUND)

    cart_item, created = Cart.objects.get_or_create(user=user, pet=pet)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    serializer = CartSerializer(cart_item)
    return Response(serializer.data)

# remove item from cart
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def remove_from_cart(request, user_id, pet_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

    try:
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        return Response({'error': 'Pet not found.'}, status=status.HTTP_404_NOT_FOUND)

    try:
        cart_item = Cart.objects.get(user=user, pet=pet)
    except Cart.DoesNotExist:
        return Response({'error': 'Item not found in cart.'}, status=status.HTTP_404_NOT_FOUND)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
        serializer = CartSerializer(cart_item)
        return Response(serializer.data)
    else:
        cart_item.delete()
        return Response({'message': 'Item removed from cart.'}, status=status.HTTP_200_OK)

# clear cart
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def clear_cart(request, user_id):
    try:
        user = User.objects.get(id = user_id)
    except User.DoesNotExist:
        return Response({"error":"User not found."}, status = status.HTTP_404_NOT_FOUND)
    Cart.objects.filter(user = user).delete()
    return Response({"message":"Cart cleared successfully."}, status = status.HTTP_200_OK)