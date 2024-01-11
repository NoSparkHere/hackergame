from django.http import HttpRequest
from django.shortcuts import redirect
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User as AuthUser
from django.contrib import messages

from server.context import Context
from server.user.interface import User

from ..models import Account

class LoginView(TemplateView):
    template_name = 'login_password.html'

    def post(self, request: HttpRequest):
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            login(self.request, user)
            return redirect('hub')
        else:
            messages.error(self.request, '用户名或密码错误')
            return redirect('password_login')

            
class SignupView(TemplateView):
    template_name = 'login_password_signup.html'

    def post(self, request: HttpRequest):
        if not self.check_form(request):
            return redirect('password_signup')
        
        account = Account.objects.create(provider='password', identity=self.request.POST['username'])
        user = AuthUser.objects.create_user(username=self.request.POST['username'], password=self.request.POST['password'])
        User.create(Context(elevated=True), group=request.POST['group'], user=user)
        account.user = user
        account.save()
        login(self.request, account.user)
        return redirect('hub')
    
    def check_form(self, request: HttpRequest):
        if not request.POST['username']:
            messages.error(self.request, '用户名不能为空')
            return False

        if not request.POST['password']:
            messages.error(self.request, '密码不能为空')
            return False

        if request.POST['password'] != request.POST['password2']:
            messages.error(self.request, '两次输入的密码不一致')
            return False

        if Account.objects.filter(identity=request.POST['username']).exists():
            messages.error(self.request, '用户名已存在')
            return False

        if request.POST['group'] not in User.groups.keys():
            messages.error(self.request, '用户组不存在')
            return False

        return True

urlpatterns = [
    path('password/login/', LoginView.as_view(), name='password_login'),
    path('password/signup/', SignupView.as_view(), name='password_signup'),
]
