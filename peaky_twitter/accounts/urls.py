from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup_view, validate_username

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', signup_view, name="signup"),
    path('validate_username/', validate_username, name='validate_username')
]
