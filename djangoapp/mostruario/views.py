from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Item
from .forms import ItemForm 

# Create your views here.

def index(request):
    if request.method == "POST" and request.user.is_authenticated:
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)  
            item.created_by = request.user
            if item.photo == None:
                item.photo = '../static/mostruario/imgs/no-image-icon.png'
                
            item.save()  
            return redirect('mostruario:index')
    else:
        form = ItemForm()

    category_filter = request.GET.get('category', 'all')
    if category_filter == 'all':
        items_list = Item.objects.all()
    else:
        items_list = Item.objects.filter(category=category_filter)
    
    paginator = Paginator(items_list, 12)  # 12 itens por página
    page = request.GET.get('page')
    
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    
    categories = Item.CATEGORIES

    return render(request, 'mostruario/index.html', {
        'form': form,
        'items': items,
        'categories': categories,
        'category_filter': category_filter  
    })

@login_required
def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id, created_by=request.user)
    item.delete()
    return HttpResponseRedirect(reverse('mostruario:index'))

@login_required
def update_item(request, item_id):
    item = get_object_or_404(Item, id=item_id, created_by=request.user)

    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mostruario:index'))
    else:
        form = ItemForm(instance=item)

    return render(request, 'mostruario/index.html', {'form': form, 'items': Item.objects.all(), 'categories': Item.CATEGORIES})