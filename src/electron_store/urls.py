from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

from . import views

from django.conf.urls import include

urlpatterns = [
    # User management
    url(r'^register/$', views.UserRegisterAPIView.as_view()),
    # url(r'^register/$', )

    # Auth
    url(r'^login/$', obtain_jwt_token, name='login'),
    url(r'^verify_login/$', verify_jwt_token, name='verify_login')
]
