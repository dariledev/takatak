from django.forms import ModelForm
from .models import *


class Communiquons_projetForm(ModelForm):
    class Meta:
        model = Communiquons_projet
        fields = '__all__'


class Soumission_clienForm(ModelForm):
    class Meta:
        model = Soumission_client
        fields = '__all__'
        