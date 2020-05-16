from django import forms

from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            "title",
            "price",
            "discount_price",
            "category",
            "description",
            "image",
        ]
        labels = {
            "title":'Title',
            "price":'Price',
            "discount_price":'Discount Price(optional)',
            "category": 'select a category',
            "description": 'Description',
            "image": 'Image',
        }
