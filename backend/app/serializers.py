from rest_framework import serializers
from .models import Pet, Cart, Order, Address, OrderItem

class PetSerializer(serializers.ModelSerializer):

    img = serializers.SerializerMethodField()

    class Meta:
        model = Pet
        fields = '__all__'

    
    def get_image(self, obj):

        try:
            if obj.img:
                return obj.img.url

        except Exception:
            pass

        return None

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'