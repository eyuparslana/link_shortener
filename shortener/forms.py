from django import forms
from shortener.models import Site


class HomeForm(forms.ModelForm):
    url = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a url...'
        }
    ))

    class Meta:
        model = Site
        fields = ('url',)