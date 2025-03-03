# from django.shortcuts import render
# from django.http import HttpResponse
# def home(request):
#     return render(request,'blog/home.html',{'title':'home'})
# def about(request):
#     return render(request,'blog/about.html', {'title':'about'})




from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Task

# Home Page (Redirect to Login)
def home(request):
    return redirect('login')

# User Registration
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('login')
    return render(request, 'blog/register.html')

# User Login
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
    return render(request, 'blog/login.html')

# User Logout
def user_logout(request):
    logout(request)
    return redirect('login')

# Show User-Specific Tasks
@login_required
def index(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'blog/index.html', {'tasks': tasks})

# Add a Task
@login_required
def add_task(request):
    if request.method == "POST":
        title = request.POST['title']
        Task.objects.create(user=request.user, title=title)
    return redirect('index')

# Toggle Task Completion
@login_required
def toggle_complete(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('index')

# Delete a Task
@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.delete()
    return redirect('index')

