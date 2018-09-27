from .models import Person, Address, Phone, Email, Group
from django import forms

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('__all__')
        widgets = {'address': forms.HiddenInput()}

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('__all__')



class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ('__all__')
        widgets = {'person': forms.HiddenInput()}

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ('__all__')
        widgets = {'person': forms.HiddenInput()}


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('__all__')






