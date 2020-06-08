

from django import forms
from .models import Lead,Billing_Details
from django_countries.widgets import CountrySelectWidget


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['full_name','corporate_email','country','phone','job_title','company','comment']
        widgets = {
            'country': forms.Select(
                attrs={
                    'class': 'form-control mb-2',
                    'name': 'country',
                }
            ),
            'full_name': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder' : "Full Name",
                    'name':'fullname',
                }
            ),
            'corporate_email': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "Corpoarate Email",
                    'name':'email',
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "Phone No.",
                    'name':'phone',
                }
            ),
            'job_title': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "Job Title",
                    'name':'job_title',
                }
            ),
            'company': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "Company",
                    'name':'company',
                }
            ),
            'comment': forms.Textarea(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "Do you have any specific field of intrest? please suggest us",
                    'rows': '3',
                    'cols': '40',
                    'name':'comment',

                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "Last Name",
                    'name': 'lastname',
                }
            ),
        }


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Billing_Details
        exclude = ['report']
        widgets = {
            'country': forms.Select(
                attrs={
                    'class': 'form-control mb-2',
                    'name': 'country',
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "First Name",
                    'name': 'First Name',
                }
            ),
            'corporate_email': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "Corpoarate Email",
                    'name': 'email',
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "Phone No.",
                    'name': 'phone',
                }
            ),
            'job_title': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "Job Title",
                    'name': 'job_title',
                }
            ),
            'company': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "Company",
                    'name': 'company',
                }
            ),
            'address': forms.Textarea(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "Address",
                    'rows': '3',
                    'cols': '40',
                    'name': 'address',

                }
            ),
            'city': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "City",
                    'name': 'city',
                }
            ),
            'state': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "State",
                    'name': 'state',
                }
            ),
            'zipcode': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "Zip Code",
                    'name': 'zipcode',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "Last Name",
                    'name': 'lastname',
                }
            )
        }
