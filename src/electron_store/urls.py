from django.conf.urls import url
from rest_framework.authtoken import views as rest_framework_views

from . import views

from django.conf.urls import include

urlpatterns = [
    url(r'^register/$', views.UserRegisterAPIView.as_view()),
    url(r'^login/$', rest_framework_views.obtain_auth_token, name='login')
]
