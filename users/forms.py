from django import forms
from .models import Profile
from core.models import Item

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            "title",
            "price",
            "discount_price",
            "category",
            "description",
            "image",
            'bought',
        ]
        labels = {
            "title":'Title',
            "price":'Price',
            "discount_price":'Discount Price(optional)',
            "category": 'select a category',
            "description": 'Description',
            "image": 'Image',
            "bought": 'is bought'

        }


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='first name')
    last_name = forms.CharField(max_length=30, label='last name')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()




class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
         'department',
         'level',
         'bio',
         'profile_picture',
         'email',
         'phone_no',
         'whatsapp_no',
         'facebook_link',
         'intagram_link',
         'twitter_link',
        ]

        labels = {
            'department': 'Department',
            'level': 'Level',
            'bio': 'Bio',
            'profile_picture': 'Profile picture',
             'email':'email address',
             'phone_no': 'mobile number',
             'whatsapp_no': 'whatsApp number',
             'facebook_link':'Facebook Address',
             'intagram_link':'Instagram Address',
             'twitter_link':'Twitter Address',
  }
