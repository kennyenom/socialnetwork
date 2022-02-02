from .models import Profile
from django import forms
from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model =  User
        fields = ['username','email','password1','password2']
       
       
    def __init__(self,*args,**kwargs):
        super(RegisterForm,self).__init__(*args, **kwargs)

        for fieldname in  ['username','email','password1','password2']:
            self.fields[fieldname].help_text = None

class Updateprofile(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']
        # help_texts = {
        #     'username': None,
        #     'email': None,
        # }

    def __init__(self,*args,**kwargs):
        super(Updateprofile,self).__init__(*args,**kwargs)
        for fieldname in ['username']:
            self.fields[fieldname].help_text = None

class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']