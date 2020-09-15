from django import forms


class ModelForm(forms.Form):
    sepal_length = forms.DecimalField(
        label='Sepal length (cm)', decimal_places=2, max_digits=3)
    sepal_width = forms.DecimalField(
        label='Sepal Width (cm)', decimal_places=2, max_digits=3)
    petal_length = forms.DecimalField(
        label='Pedal length (cm)', decimal_places=2, max_digits=3)
    petal_width = forms.DecimalField(
        label='Pedal Width (cm)', decimal_places=2, max_digits=3)
