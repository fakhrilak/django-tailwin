from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns=[
    url(r'^$',views.instagram),
    url(r'^user/$',views.getUser),
    url(r'(?P<id>[\w\.-]+)/$',views.detailPost),
]