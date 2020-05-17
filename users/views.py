from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile
from core.models import Item
from django.core.paginator import Paginator



def user_profile(request):
    user = request.user
    items = Item.objects.filter(owner=request.user)
    active_items = Item.objects.filter(owner=request.user).filter(bought = False)
    sold_items = Item.objects.filter(owner=request.user).filter(bought = True)
    active_items_counts = active_items.count()
    sold_items_counts = sold_items.count()
    item_count = items.count()
    context ={
        'user':user,
        'active_items_counts': active_items_counts,
        'sold_items_counts': sold_items_counts,
        'item_count': item_count
    }
    return render(request, "users/profile.html", context)

def update_profile(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    if request.method != 'POST':
        form = ProfileForm(instance = profile)
    else:
        form = ProfileForm(request.POST, request.FILES, instance = profile)
        if form.is_valid():
            update = form.save(commit=False)
            update.user = request.user
            update.save()
            return redirect('users:profile')
    context = {
            'form':form
    }
    return render(request, 'users/update_profile.html', context)




def user_items(request):
    items = Item.objects.filter(owner=request.user).filter(bought = False)
    for item in items:
        item.price = f'{item.price:,}'
    paginator = Paginator(items, 16)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    item_count = items.count()
    context = {
        'items':items,
        'item_count':item_count,
        'page_obj':page_obj

    }
    return render(request, "users/user_items.html", context)

def sold_items(request):
    items = Item.objects.filter(owner=request.user).filter(bought = True)
    for item in items:
        item.price = f'{item.price:,}'
    paginator = Paginator(items, 16)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    item_count = items.count()
    context = {
        'items':items,
        'page_obj':page_obj,
        'item_count':item_count,

    }
    return render(request, "users/sold_items.html", context)
