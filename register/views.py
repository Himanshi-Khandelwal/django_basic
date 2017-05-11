from django.shortcuts import render, redirect , get_object_or_404,redirect,render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from forms import SignUpForm, Form
from .models import images
from urllib import quote_plus
# Create your views here.

def base(request):
    context = RequestContext(request)
    return render_to_response('base.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('base')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def post_create(request):
    form = Form(request.POST or None,request.FILES or None)
    context = {
        "form": form,
    }
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user=request.user
        instance.save()
        # message success
        return render(request, "show.html",context)
    
    return render(request, "profile.html", context)

def show_list(request): #list items
    queryset_list = images.objects.all()
    query=request.GET.get("q")
    if query:
        queryset_list=queryset_list.filter(title__icontains=query)
   
    context = {
        "object_list": queryset_list,
        "title": "List"
            }
    return render(request, "show.html", context)

def detail(request,id=None): #retrieve
    context = RequestContext(request)
    return render_to_response('detail.html', context)
