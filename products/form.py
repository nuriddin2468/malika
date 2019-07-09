from django.forms import ModelForm
from django.forms.widgets import TextInput
from .models import SmartPhoneModel


class SmartPhoneModelForm(ModelForm):
    class Meta:
        model = SmartPhoneModel
        fields = '__all__'
        widgets = {
            'color': TextInput(attrs={'type':'color'}),
        }
