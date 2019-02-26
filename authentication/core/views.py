from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def home(request):
    count=User.objects.count()
    return render(request,'home.html',{'count':count})


def signup(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.info(request,f"Congratulations!  Account Created For {username}!")
            return redirect('login')
    else:
        form=UserCreationForm()
    return render(request,'registration/signup.html',{'form':form})

@login_required
def content(request):
    return render(request,'content.html')
