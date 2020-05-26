from django.contrib import admin

# Register your models here.
from .models import Item, Category, ItemGallery


admin.site.register(Item)
admin.site.register(Category)
admin.site.register(ItemGallery)
