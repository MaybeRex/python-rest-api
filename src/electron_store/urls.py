from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

from .views import user as userViews
from .views import image as imageViews

from django.conf.urls import include

urlpatterns = [
    # User management
    url(r'^register/$', userViews.UserRegisterAPIView.as_view()),
    url(r'^profile/(?P<username>[\w.@+-]+)/$', userViews.UserUpdateAPIView.as_view()),

    # Images
    url(r'^images/$', imageViews.UserImageUploadAPIView.as_view()),

    # Auth
    url(r'^login/$', obtain_jwt_token, name='login'),
    url(r'^verify_login/$', verify_jwt_token, name='verify_login')
]
