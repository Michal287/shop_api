from rest_framework import routers
from .user.views import UserViewSet, RegisterView
from django.urls import path
from rest_framework.authtoken import views

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', views.obtain_auth_token, name='login'),
]

router = routers.SimpleRouter()

router.register(r'user', UserViewSet)

urlpatterns += router.urls

