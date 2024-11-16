from django import forms
from .models import Enquiry, Book, CustomUser
from django.contrib.auth.models import Group
from django.http import request

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['first_name', 'last_name', 'email', 'phone', 'book', 'message']

    def __init__(self, *args, **kwargs):
        super(EnquiryForm, self).__init__(*args, **kwargs)
        self.fields['book'].queryset = Book.objects.filter(status='published')
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['phone'].widget.attrs['placeholder'] = 'Phone'
        self.fields['message'].widget.attrs['placeholder'] = 'Message'


class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'phone', 'password', ]

    password = forms.CharField(widget=forms.PasswordInput)

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.user_type = 'customer'
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()

        group = Group.objects.get(name='Customers')
        user.groups.add(group)
        return user

