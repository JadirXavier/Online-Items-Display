from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Item, ItemPhoto
from .forms import ItemForm 

def index(request):
    ItemPhotoFormSet = inlineformset_factory(Item, ItemPhoto, fields=['photo'], extra=3, can_delete=False)

    if request.method == "POST" and request.user.is_authenticated:
        form = ItemForm(request.POST, request.FILES)
        formset = ItemPhotoFormSet(request.POST, request.FILES)

        if form.is_valid() and formset.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            formset.instance = item
            formset.save()

            return redirect('mostruario:index')
    else:
        form = ItemForm()
        formset = ItemPhotoFormSet()

    category_filter = request.GET.get('category', 'all')
    sort_order = request.GET.get('sort', 'name_asc')

    if category_filter == 'all':
        items_list = Item.objects.all()
    else:
        items_list = Item.objects.filter(category=category_filter)

    if sort_order == 'name_asc':
        items_list = items_list.order_by('name')
    elif sort_order == 'name_desc':
        items_list = items_list.order_by('-name')
    elif sort_order == 'price_asc':
        items_list = items_list.order_by('price')
    elif sort_order == 'price_desc':
        items_list = items_list.order_by('-price')

    paginator = Paginator(items_list, 12)  #itens por página
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
        'formset': formset,
        'items': items,
        'categories': categories,
        'category_filter': category_filter,
        'sort_order': sort_order
    })

@login_required
def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id, created_by=request.user)
    item.delete()
    return HttpResponseRedirect(reverse('mostruario:index'))

    
@login_required
def update_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    ItemPhotoFormSet = inlineformset_factory(Item, ItemPhoto, fields=['photo'], extra=3, can_delete=False)

    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES, instance=item)
        formset = ItemPhotoFormSet(request.POST, request.FILES, instance=item)

        if form.is_valid() and formset.is_valid():
            form.save()
            
            existing_photos = list(item.photos.all())  
            
            for i, form in enumerate(formset.forms):
                if form.cleaned_data.get('photo'):
                    if i < len(existing_photos):
                        existing_photos[i].photo.delete(save=False)
                        existing_photos[i].photo = form.cleaned_data['photo']
                        existing_photos[i].save()
                    else:
                        ItemPhoto.objects.create(item=item, photo=form.cleaned_data['photo'])
                elif i < len(existing_photos):
                    existing_photos[i].save()

            if len(existing_photos) > len(formset.forms):
                for photo in existing_photos[len(formset.forms):]:
                    photo.delete()

            return redirect('mostruario:index')
    else:
        form = ItemForm(instance=item)
        formset = ItemPhotoFormSet(instance=item)

    items = Item.objects.all()
    categories = Item.CATEGORIES

    return render(request, 'mostruario/update.html', {
        'form': form,
        'formset': formset,
        'items': items,
        'categories': categories,
    })

def logout_view(request):
    logout(request)
    return redirect('mostruario:index')
