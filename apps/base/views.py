from django.shortcuts import render,redirect
from apps.base.models import *
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import PasswordChangeForm
from django.core.exceptions import ValidationError

from django.contrib.auth import authenticate, login


def index(request):
    settings = Settings.objects.latest('id')
    blog = News.objects.all()
    post = Blogpost.objects.all()
    widget = Widget.objects.all()
    return render(request, "demo25.html", locals())

def blog(request, id):
    blog = News.objects.get(id=id)
    comments = blog.comments.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        user_comment = request.POST.get('comment')
        author, created = User.objects.get_or_create(username=name)
        
        if created or not Review.objects.filter(name=author, comment=user_comment).exists():
            new_comment = Review(name=author, comment=user_comment)
            new_comment.save()
            blog.comments.add(new_comment)

        new_comment = Review(name=name,comment=user_comment)
        new_comment.save()

        blog.comments.add(new_comment)
        return redirect('#/', id=id)

    return render(request, "blog-post.html", locals())


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        try:
            validate_password(password)
        except ValidationError as e:
            return render(request, 'signup.html', {'error_message': e})
        
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'username_exists': True})
        
        user = User.objects.create_user(username=username, email=email, password=password)
     
        login(request, user)
        return redirect('/')  
    else:
        return render(request, 'signup.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  
        else:
            return render(request, 'signin.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'signin.html')