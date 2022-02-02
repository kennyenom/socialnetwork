from multiprocessing import context
from sre_parse import FLAGS
from django.http import HttpResponse
from django.shortcuts import render,redirect,HttpResponse
from django.urls import *
from django.contrib import messages
from django.urls import reverse
from .forms import *
# Create your views here.


def index(request,*args,**kwargs):
    post = PostModel.objects.all()
    form = Post()

    context = {
        'posts':post,
        'form':form
    }
    return render(request,'blog/index.html',context)

def about(*args,**kwargs):
    return HttpResponse('<h2>blog about </h2>')

 
# def add_blog(request):
    
#     try:
#         if request.method == 'POST':
#             form = Post(request.POST)
#             print(request.FILES)
#             image = request.FILES['image']
#             title = request.POST.get('title')
#             user = request.user
            
#             if form.is_valid():
#                 content = form.cleaned_data['content']
#                 form.save()
            
#             blog_obj = PostModel.objects.create(
#                 user = user , title = title, 
#                 content = content, image = image
#             )
#             print(blog_obj)
#             return redirect('blog-home')
            
            
    
#     except Exception as e :
#         print(e)
#     context = {'form' :form}
#     return render(request , 'blog/post_form.html' , context)

def newpost(request):
    p_form = Postimage( request.POST or None, request.FILES or None, instance=request.user)
    if request.method == 'POST':
        form = Post(request.POST,request.FILES)
        if form.is_valid() and p_form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('blog-home')
    else:
        form = Post()

    context = {
     
        'form':form,
        # 'p_form':p_form,
        
    }
    return render(request,'blog/post_form.html',context)

def post_detail(request,pk):
    comment = Comment.objects.all()
    post = PostModel.objects.get(pk=pk)
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.post = post
            instance.user = request.user
            instance.save()
            return redirect('blog-detail' ,pk=post.id)
    else:
         c_form=CommentForm()
    context = {
        'post':post,
        'c_form':c_form,
        'com':comment

    }
    return render(request,'blog/post_detail.html',context)

def post_delete(request,pk):
    post =PostModel.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog-home')
    
    context = {
        'post':post
    }
    

    return render(request,'blog/post_delete.html',context)

def post_edit(request,pk):
    post = PostModel.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostEdit(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog-detail', pk=pk)
    else:
        form = PostEdit(instance=post)

    context = {
        'form':form
    }
    return render(request,'blog/post_edit.html',context)


def comments(request):
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.user = request.user
            instance.save()

    else:
        c_form = CommentForm()

    return reverse('blog-detail')