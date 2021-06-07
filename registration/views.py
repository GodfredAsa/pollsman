from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404,render,redirect
from django.http import HttpResponse, Http404

from django.contrib.auth import authenticate, login

from django.urls import reverse

from .forms import User
#from django.contrib.auth.forms import UserCreationForm, UserAuthenticationForm
from django.contrib.auth import login,logout


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('registration:home')
    else:
        form = UserCreationForm()
    
    return render(request,'signup.html',{'form':form})

# SIGN PAGE OF THE THE REGISTRATION APP
def sign_in(request):
    # if request.method == POST:
        # form = UserAuthenticationForm(request.POST)

    # username = request.POST.get('username', False)
    # password = request.POST.get('password', False)
    # user = authenticate(request, username = username,  password = 'password')
    # if user is not None:
        # login(request, user)
    # else:
        # user = UserCreationForm()
    template = 'sign_in.html'
    #context = {'form': form}
    return render(request,template)
    
    
    # 
# def signup(request):
    # return HttpResponse('Hello World')
        

#  form  = BlogEntryForm(request.POST)
#  if form.is_valid():
    #  form.save()
#  template = 'blog/blog.html'
#  context = {'form': form}
#  return render(request, template, context)

