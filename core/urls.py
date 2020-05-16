from django.urls import path

from .views import (
        #HomeView,
        categories,
        spec_category,
        itemdetail,
        add_new_item,
        edit_item,
        contact_merchant,
        welcome,
        search_item,
        home_page

)




app_name = 'core'

urlpatterns = [
    path('', welcome, name = 'welcome'),
    #path('Home/', HomeView.as_view(), name='home'),
    path('Home/', home_page, name='home'),
    path('product/<slug>/', itemdetail, name='product'),
    path('categories/', categories, name='category'),
    path('categories/<slug>/', spec_category, name='spec_category'),
    path('collegetrade/new_item/', add_new_item, name='new_item'),
    path('edit_item/<item_id>/', edit_item, name='edit_item'),
    path('contact_merchant/<slug>/', contact_merchant, name = 'contact_merchant'),
    path('search/', search_item, name='search_item')

]
