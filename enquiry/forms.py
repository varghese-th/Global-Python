from django import forms

from .models import Enquiry

class EnquiryCreationForm(forms.ModelForm):

    class Meta:
        model = Enquiry
        fields = ('name', 'address', 'contact', 'email', 'enquiry',)