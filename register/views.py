from django.shortcuts import render, redirect , get_object_or_404,redirect,render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import login, authenticate
from forms import SignUpForm, Formss
from .models import images
from urllib import quote_plus
from django.contrib.auth.models import User
from django.contrib.auth import logout as django_logout
# Create your views here.

def base(request):
    context = RequestContext(request)
    return render_to_response('base.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
           # form.save()
	    user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
           # username = form.cleaned_data.get('username')
            #raw_password = form.cleaned_data.get('password2')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            return redirect('base')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def post_create(request):
    form = Formss(request.POST or None,request.FILES or None)
    context = {
        "form": form,
    }
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user=request.user
        instance.save()
        # message success

        return redirect("/show_list/")

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

def logout_view(request):
    django_logout(request)
    return redirect("/")
