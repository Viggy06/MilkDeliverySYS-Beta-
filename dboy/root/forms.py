from django import forms
from .models import FixedForAll, Delivery_Boy_Model

class FixedForAllForm(forms.ModelForm):
    class Meta:
        model = FixedForAll
        fields = "__all__"

class Dboy_form(forms.ModelForm):
    class Meta:
        model = Delivery_Boy_Model
        exclude = ['group', 'order']

