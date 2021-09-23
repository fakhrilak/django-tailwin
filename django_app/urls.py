from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^instagram/',include('instagram.urls')),
    url(r'^twitter/',include('twitter.urls')),
    url(r'^',views.docs),
]
