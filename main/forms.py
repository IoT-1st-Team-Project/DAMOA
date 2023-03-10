from django.forms import ModelForm
from models import *

class ClubForm(ModelForm):
    class Meta:
        model = Club
        fields = []

