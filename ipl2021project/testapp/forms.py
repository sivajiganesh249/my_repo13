from django import forms
from testapp.models import Player
class PlayerForm(forms.ModelForm):
    class Meta:
        model=Player
        fields='__all__'
