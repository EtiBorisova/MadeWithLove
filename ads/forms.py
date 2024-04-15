from django import forms

from MadeWithLove.ads.models import AdsModel


class CreateAdForm(forms.ModelForm):
    class Meta:
        model = AdsModel
        exclude = ['seller']
