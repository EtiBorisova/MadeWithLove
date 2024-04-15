from django import forms


class SearchForm(forms.Form):
    product = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search product',
                'class': 'search-form',

            }

        )

    )


