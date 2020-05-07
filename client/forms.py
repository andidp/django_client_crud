from django.forms import ModelForm
from .models import ClientModel


class ClientForm(ModelForm):
    class Meta:
        model = ClientModel
        fields = '__all__'
