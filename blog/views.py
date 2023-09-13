from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from . models import Post, Profile
from . forms import UpdateForm, SignupForm

def home(request):
    posts = Post.objects.all()[0:5]
    return render(request, 'home.html', {'posts': posts})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'detail.html', {'post': post})

def creation(request):
    if request.method == 'POST':
        form = UpdateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Posted created successfully')
        return redirect('home')
    
    else:
        form = UpdateForm()
    return render(request, 'creation.html', {'form':form})

def update(request, pk):
    posting = Post.objects.get(pk=pk)
    form = UpdateForm()

    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=posting)

        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully')
            return redirect('home')

    else:
        form = UpdateForm(instance=posting)

    return render(request, 'update.html', {'posting': posting, 'form': form})


def delete(request, pk):
    list = Post.objects.get(pk=pk)

    if request.method == 'POST':
        list.delete()
        messages.success(request, 'Post deleted')
        return redirect('home')
    
    return render(request, 'delete.html', {'list': list})



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hello {username} your account was created successfully Login')
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form':form})


def profile(request):
    return render(request, 'profile.html')
    
    


