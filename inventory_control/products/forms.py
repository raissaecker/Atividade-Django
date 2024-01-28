from django import forms
from .models import Product
import re

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ["thumbnail", "slug", "is_perishable"]

        labels = {
            "name": "Nome",
            "description": "Descrição",
            "sale_price": "Preço",
            "expiration_date": "Data de expiração",
            "photo": "Imagem",
            "enabled": "Ativo",
            "category": "Categoria"
        }

        error_messages = {
            "name": {
                "required": "O campo nome é obrigatório",
                "unique": "Já existe um produto com esse nome"
            },
            "description": {
                "required": "O campo descrição é obrigatório"
            },
            "sale_price": {
                "required": "O campo preço é obrigatório"
            }
        }

        widgets = {
            "expiration_date": forms.DateInput(attrs={"type":"date"}, format="%Y-%m-%d")
        }

    