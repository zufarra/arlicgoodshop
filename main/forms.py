from django.forms import ModelForm
from main.models import ItemEntry
from django.utils.html import strip_tags

class ItemEntryForm(ModelForm):
    class Meta:
        model = ItemEntry
        fields = ["name", "price", "description"]
    def clean_itemName(self):
        item = self.cleaned_data["name"]
        return strip_tags(item)

    def clean_price(self):
        price = self.cleaned_data["price"]
        return strip_tags(price)
    
    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)