from django.shortcuts import render
from apps.base.models import Settings, News
# Create your views here.

def index(request):
    settings = Settings.objects.latest('id')
    blog = News.objects.all()
    return render(request, "demo25.html", locals())

def blog(request, id):
    blog = News.objects.get(id=id)
    return render(request, "blog-post.html", locals())
