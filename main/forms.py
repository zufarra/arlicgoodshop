from django.forms import ModelForm
from main.models import Application

class ShopEntryForm(ModelForm):
    class Meta:
        model = Application
        fields = ["name", "price", "description"]