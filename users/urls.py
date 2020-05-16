from django.urls import path

from .views import (
        user_profile,
        update_profile,
        user_items,
        sold_items,
)

app_name = 'users'

urlpatterns = [
    path('profile/', user_profile, name='profile'),
    path('profile_update/<profile_id>/', update_profile, name = 'update_profile'),
    path('profile/my_items/', user_items, name = 'user_items'),
    path('profile/my_sold_items/', sold_items, name = 'sold_items'),

]
