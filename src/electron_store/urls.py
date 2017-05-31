from django.conf.urls import url
from . import views

from django.conf.urls import include

urlpatterns = [
    url(r'^register', views.UserRegisterAPIView.as_view()),
    url(r'^login', views.UserLoginAPIView.as_view()),
]
