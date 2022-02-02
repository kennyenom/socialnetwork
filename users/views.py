
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-login')
    
    else:
        form = RegisterForm()
    return render(request,'users/signup.html',{'form':form})

@login_required
def profile(request,*args,**kwargs):
    if request.method == 'POST':
        u_form = Updateprofile(request.POST,instance=request.user)
        p_form = ProfileUpdate(request.POST or None,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('blog-profile')
    else :
        u_form = Updateprofile(instance=request.user)
        p_form= ProfileUpdate(instance=request.user.profile)
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'users/profile.html',context)

# def updateprofile(request):
#     return render(request,'')
