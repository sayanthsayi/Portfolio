from django import forms
from django . forms import ModelForm
from . models import contact

class ContactForm(ModelForm):
    first_name = forms.CharField(max_length=250,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    second_name = forms.CharField(max_length=250,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Second Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Phone'}))
    message = forms.CharField(max_length=500,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Tell Me'}))

    class Meta:
        model = contact
        fields = "__all__"

