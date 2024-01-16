from django.contrib.auth.views import PasswordResetView
from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, RegisterView, logout_user, ConfirmUserView, UserProfileView, UserForgotPasswordView, \
    UserPasswordResetConfirmView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('confirm_email/<str:uuid>', ConfirmUserView.as_view(), name='confirm_register'),
    path('user_pfofile/', UserProfileView.as_view(), name='user_profile'),
    path('password-reset/', UserForgotPasswordView.as_view(), name='password_reset'),
    path('set-new-password/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]