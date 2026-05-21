from django.contrib import admin

from .models import UserProfile, Pet, Cart, Order, OrderItem

# # Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'password', 'phone', 'is_active', 'is_staff')

@admin.register(Pet)
class PetsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'type',
        'category',
        'age',
        'gender',
        'price',
        'breed_info',
        'img',
        'desc',
        'health',
        'behavior',
        'care',
        'extra',
        'seller'
    )
    list_filter = ('type', 'category', 'age')
    search_fields = ('name', 'description')
    
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):      
    list_display = ('id', 'user', 'pet', 'quantity')
    list_filter = ('user',)
    search_fields = ('user__email', 'pet__name')

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'created_at',
        'address',
        'total_price',
        'status',
        'user'
    )
    search_fields = ('address','user')
    list_filter = ('created_at','status')
    inlines = [OrderItemInline]
