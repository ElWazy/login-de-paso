from django import forms
from credenciales.models import Credenciales


class CredencialesForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        external_value = cleaned_data.get('rut')

        internal_value = external_value.replace('.', '').strip('.')

        cleaned_data['rut'] = internal_value

        return cleaned_data


    class Meta:
        model = Credenciales
        fields = ['rut', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

