from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'photo', 'price', 'category']

    def __init__(self, *args, **kwargs):
            super(ItemForm, self).__init__(*args, **kwargs)

            self.fields['name'].widget.attrs.update({
                'placeholder': 'Digite o nome do item',  
            }) 

            self.fields['price'].widget.attrs.update({
                'required': 'required',
                'min': '0.01',
                'type': 'number',
                'step': '0.01',
                'placeholder': 'Digite o preço',
                'oninvalid': "this.setCustomValidity('Por favor, insira um preço positivo maior que zero.')",
                'oninput': "this.setCustomValidity('')"  
            })
