from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
def register(request):
    return render(request,'blog/home.html',{'title':'home'})


# Create your views here.
