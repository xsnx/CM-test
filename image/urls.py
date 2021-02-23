from django.urls import path
from rest_framework.authtoken import views
from image.views import DownloadImage


urlpatterns = [
    path('downloadimage', DownloadImage.as_view()),
    path('api_token_auth', views.obtain_auth_token, name='auth-token'),
]
