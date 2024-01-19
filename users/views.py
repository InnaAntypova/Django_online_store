from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as BaseLoginView, PasswordResetView, PasswordResetConfirmView
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, UpdateView

from django_online_store import settings
from users.forms import RegisterForm, UserProfileForm, UserForgotPasswordForm, UserSetNewPasswordForm
from users.models import User


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


def logout_user(request):
    logout(request)
    return redirect('catalog:index')


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('catalog:index')
    template_name = 'users/register.html'

    def form_valid(self, form):
        if form.is_valid():
            user = form.save()
            domain = 'http://127.0.0.1:8000/'

            send_mail(
                f'Подтверждение регистрации для {user.email}',
                f"""Вы зарегистрировались на сайте Dominion Store. Необходимо подтвердить Ваш аккаунт по ссылке \n
                {domain}{reverse('users:confirm_register', kwargs={'uuid':user.field_uuid})}""",
                settings.EMAIL_HOST_USER,
                [user.email]
            )
        return super().form_valid(form)


class ConfirmUserView(View):

    def get(self, request, uuid):
        try:
            user = User.objects.get(field_uuid=uuid)
            user.is_active = True
            user.has_perm('catalog.view_product')
            user.has_perm('blog.view_product')
            user.save()
            return render(request, 'users/confirm_register.html')
        except User.DoesNotExist:
            return render(request, 'users/error_register.html')


# class ResetUserPassword(View):
#     form_class = ResetPassForm
#     template_name = 'users/user_password_reset.html'
#
#     # def get_queryset(self):
#     #     queryset = super().get_queryset()
#     #     queryset = queryset.
#     #     return queryset
#     def form_valid(self, form):
#         if form.is_valid():
#             user = form.save()
#             user_ = User.objects.get(email=user.email)
#             new_pass = User.objects.make_random_password(length=8)
#             user_.set_password(new_pass)
#
#             send_mail(
#                 f'Смена пароля для  {user.email}',
#                 f""" Для Вас сгенерирован новый пароль: \n
#                 {new_pass}""",
#                 settings.EMAIL_HOST_USER,
#                 [user.email]
#             )
#
#         return super().form_valid(form)

# def reset_password(request):
#     if request.method == 'POST':
#         email = request.method.get('email')
#         user = User.objects.get(email=email)
#         new_pass = User.objects.make_random_password(length=8)
#         send_mail(
#                 f'Смена пароля для  {email}',
#                 f""" Для Вас сгенерирован новый пароль: \n
#                         {new_pass}""",
#                 settings.EMAIL_HOST_USER,
#                 [email]
#             )
#
#         user.set_password(new_pass)
#
#     return render(request, 'users/login.html')


# def reset_password(request):
#     new_pass = User.objects.make_random_password(length=8)
#     request.user.set_password(new_pass)
#     request.user.save()
#     send_mail(
#             f'Смена пароля для  {request.user.email}',
#             f""" Для Вас сгенерирован новый пароль: \n
#             {new_pass}""",
#             settings.EMAIL_HOST_USER,
#             [request.user.email]
#             )
#     return redirect(reverse('users:login'))


class UserProfileView(LoginRequiredMixin, UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserProfileForm

    def get_object(self, queryset=None):
        return self.request.user


class UserForgotPasswordView(PasswordResetView):
    form_class = UserForgotPasswordForm
    template_name = 'users/user_password_reset.html'
    success_url = reverse_lazy('catalog:index')
    success_message = 'Письмо с инструкцией по восстановлению пароля отправлена на ваш email'
    subject_template_name = 'users/password_subject_reset_mail.txt'
    email_template_name = 'users/password_reset_mail.html'


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = UserSetNewPasswordForm
    template_name = 'users/user_password_set_new.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Пароль успешно изменен. Можете авторизоваться на сайте.'


