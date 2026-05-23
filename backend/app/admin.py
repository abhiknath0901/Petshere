from django.contrib import admin

from .models import UserProfile, Pet, Cart, Order, OrderItem, Address

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
    search_fields = ('name', 'desc', 'breed_info', 'seller')
    
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

        'id',

        'user',

        'address',
        'ordered_items',

        'total_price',

        'payment_status',

        'status',

        'created_at'
    )

    search_fields = (

        'user__email',

        'address__receiver_name',

        'address__city'
    )

    list_filter = (

        'status',

        'payment_status',

        'created_at'
    )

    inlines = [OrderItemInline]
    def ordered_items(self, obj):

        return ", ".join([

            item.pet.name
            for item in obj.items.all()

        ])

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):

    list_display = (

        'receiver_name',

        'receiver_phone',

        'city',

        'state',

        'user'
    )

    search_fields = (

        'receiver_name',

        'receiver_phone',

        'city',

        'state',

        'user__email'
    )