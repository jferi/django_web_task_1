from django import forms
from .models import Velemeny

class VelemenyForm(forms.ModelForm):
    class Meta:
        model=Velemeny
        fields=['nev','szoveg']
        labels={'nev':'Név:','szoveg':'Vélemény:'}
        widgets={'nev':forms.TextInput(attrs={'size':30,'style':'width:100%','class':'form-control'}),
                 'szoveg':forms.TextInput(attrs={'size':30,'style':'width:100%','class':'form-control'})}
