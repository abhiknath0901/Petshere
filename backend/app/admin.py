from django.contrib import admin

from .models import Pet

# Register your models here.
@admin.register(Pet)
class PetsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'type',
        'category',
        'age',
        'gender',
        'price',
        'breed_info',
        'img',
        'description',
        'health',
        'behavior',
        'care',
        'extra',
        'seller'
    )
   