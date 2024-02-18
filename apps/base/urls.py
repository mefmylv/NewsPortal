from django.urls import path
from apps.base.views import index, blog
urlpatterns = [
    path('', index , name='index'),
    path('blog/<int:id>//', blog , name='blog')

]
