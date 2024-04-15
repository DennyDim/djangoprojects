from django  import forms

from user.models import Profile


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['username', 'email', 'age']

        widgets = {
            'username': forms.TextInput(
                attrs={'placeholder': "Username"}
            ),
            'email': forms.EmailInput(
                attrs={'placeholder': "Email"}
            ),
            "age": forms.NumberInput(
                attrs={'placeholder': "Age", 'step': 'any',
                       'style': 'appearance: textfield;'}
            )
        }

