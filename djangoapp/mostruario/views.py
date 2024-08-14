from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Item
from .forms import ItemForm 

def item_list(request):
    items = Item.objects.all()
    paginator = Paginator(items, 40)  # 5 colunas x 8 fileiras = 40 itens por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'mostruario/item_list.html', {'page_obj': page_obj})

@login_required
def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'mostruario/item_form.html', {'form': form})

@login_required
def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.user != item.created_by:
        return redirect('item_list')
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'mostruario/item_form.html', {'form': form})


# Create your views here.
