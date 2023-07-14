from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Signup,house
class signup_form(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={ 'id':"signup-user" ,'type':"text", 'class':"input", 'placeholder':"Create your Username"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'input','id':'signup-pass','type':'password', 'placeholder':"enter your password"}))
    reppass=forms.CharField(widget=forms.PasswordInput(attrs={'class':'input','id':'repeat-pass','type':'password','placeholder':"confirm password"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'id':"signup-email", 'type':"text", 'class':"input", 'placeholder':"Enter your email address"}))
    def clean(self):
        x=super().clean()
        pas=x['password']
        rep=x['reppass']
        if pas!=rep:
            raise ValidationError("Passwords do not match")

    class Meta:
        model=User
        fields=('username','password','reppass','email')
class formss(forms.ModelForm):
    class Meta:
        model=Signup
        fields=()
class addhouse(forms.ModelForm):
    owner=forms.CharField(widget=forms.TextInput(attrs={'type':'text'}))
    contact=forms.IntegerField(widget=forms.NumberInput(attrs={'min':0,'type':'number'}))
    CHOICES=[
        ('1BHK','1BHK'),
        ('2BHK','2BHK'),
        ('3BHK','3BHK')
    ]
    price=forms.IntegerField(widget=forms.NumberInput(attrs={'min':0,'type':'number'}))
    type=forms.CharField(widget=forms.RadioSelect(choices=CHOICES))
    apartment=forms.CharField()
    address=forms.CharField()
    img1=forms.ImageField(required=False)
    img2=forms.ImageField(required=False)
    img3=forms.ImageField(required=False)
    class Meta:
        model=house
        fields=('owner','contact','type','address','price','apartment','img1','img2','img3')

class password_reset(forms.Form):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'min':6,'id':'password','name':'password'}))
    reppass=forms.CharField(widget=forms.PasswordInput(attrs={'min':6,'id':'reppass','name':'reppass'}))
    def clean(self):
        x=super().clean()
        if x['password']!=x['reppass']:
            raise ValidationError("passwords do not match")
