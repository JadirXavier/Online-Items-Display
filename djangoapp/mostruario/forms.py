from django import forms
from .models import Item, ItemPhoto

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ['name', 'price', 'category']  

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'placeholder': 'Digite o nome do item'
        })
        self.fields['price'].widget.attrs.update({
            'min': '0.01',
            'max': '9999.99',
            'type': 'number',
            'step': '0.01',
            'placeholder': 'Digite o preço',
            'oninvalid': "this.setCustomValidity('Por favor, insira um preço entre 0 e R$10000.')",
            'oninput': "this.setCustomValidity('')"  
        })

    def save(self, commit=True):
        item = super(ItemForm, self).save(commit=False)
        if self.user:
            item.created_by = self.user
        if commit:
            item.save()
        return item