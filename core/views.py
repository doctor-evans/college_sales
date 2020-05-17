from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from .models import Item, Category
from .forms import ItemForm
from users.forms import EditItemForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.core.paginator import Paginator


def home_page(request):
    items = Item.objects.order_by('-date_added').filter(bought = False)
    for item in items:
        item.price = f'{item.price:,}'
    paginator = Paginator(items, 16)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'items':items,
        'page_obj':page_obj
    }
    return render(request, 'core/home.html', context)



def search_item(request):
    search = request.GET.get('search_box')
    items = Item.objects.filter(title__icontains= search[:3]).filter(bought = False).order_by('-date_added')
    for item in items:
        item.price = f'{item.price:,}'
    paginator = Paginator(items, 16)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'items':items,
        'page_obj':page_obj,
        'search':search,
    }
    return render(request, 'core/search.html', context)


def itemdetail(request, slug):
    item = Item.objects.get(id=slug)
    item.price = f'{item.price:,}'
    related = Item.objects.filter(owner=item.owner).exclude(id=slug)
    related_items = related.filter(bought = False)[::-1][:3]
    context = {
     'item':item,
     'related_items':related_items,
    }
    return render(request, "core/product.html", context)

def contact_merchant(request, slug):
    item = Item.objects.get(id = slug)
    context = {
        'item': item
    }
    return render(request, "core/contact_merchant.html", context)


def categories(request):
    categories = Category.objects.all()
    context = {
    'categories': categories
        }
    return render(request, "core/category.html", context)


def spec_category(request, slug):
    category = Category.objects.get(text = slug)
    items = category.item_set.order_by('-date_added').filter(bought = False)
    for item in items:
        item.price = f'{item.price:,}'
    paginator = Paginator(items, 16)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'category':category,
        'items':items,
        'page_obj':page_obj
    }
    return render(request, 'core/specific_category.html', context)

@login_required
def add_new_item(request):
    if request.method != 'POST':
        form = ItemForm()
    else:
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.owner = request.user
            new_item.save()
            return redirect('core:home')
    context = {
            'form':form
    }
    return render(request, 'core/new_item.html', context)


def edit_item(request, item_id):
    item = Item.objects.get(id = item_id)
    if item.owner != request.user:
        raise Http404

    if request.method !='POST':
        form = EditItemForm(instance = item)
    else:
        form = EditItemForm(request.POST, request.FILES, instance = item)
        if form.is_valid():
            form.save()
            return redirect('users:user_items')
    context = {
            'form': form
    }
    return render(request, 'core/edit_item.html', context)


def welcome(request):
    return render(request, 'core/welcome.html')
