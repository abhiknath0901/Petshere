from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Pet , Cart, Order
from .serializers import PetSerializer, CartSerializer, OrderSerializer
User = get_user_model()


# Create a new user
@api_view(['POST'])
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

# Get all pets
@api_view(['GET'])
def get_pets(request):
    pets = Pet.objects.all()
    serializer = PetSerializer(pets, many=True)
    return Response(serializer.data)

# Get cart items for a user
@api_view(['GET'])
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

