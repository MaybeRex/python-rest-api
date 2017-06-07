from django.conf.urls import url
from . import views

urlpatterns = [
    # heartbeat
    url(r'^r/$', views.UserRegisterAPIView.as_view()),
    url(r'^profile/(?P<username>[\w.@+-]+)/$', views.UserUpdateAPIView.as_view()),
    # url(r'^register/$', )

    # Auth
    url(r'^login/$', obtain_jwt_token, name='login'),
    url(r'^verify_login/$', verify_jwt_token, name='verify_login')
]
