from django import forms
from postupload.models import MyUser
from django.contrib.auth.forms import UserCreationForm

from postupload.models import Postuploads



class RegistrationForm(UserCreationForm):
    class Meta():
        model=MyUser
        fields=['first_name','last_name','username','email',
        'phone','profile_pic','password1','password2']

class LoginForm(forms.Form):                
    username=forms.CharField(widget=forms.TextInput(attrs={"class=col":"form-control","placeholder":"enter username","aria-label":"username"}))      #attrs=attribute
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class=col":"form-control","placeholder":"enter password"}))

class PostuploadForm(forms.ModelForm):
    class Meta():
        model=Postuploads
        fields=['image','caption']

        widgets={
             "image":forms.FileInput(attrs={"class":"form-select mt-5"}),
             "caption":forms.Textarea(attrs={"class":"form-control border border-light mt-5","placeholder":"write a caption...","rows":1})
     
        }