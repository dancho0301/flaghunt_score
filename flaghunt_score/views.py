from django.shortcuts import render
from django.contrib.auth.views import LoginView as AuthLoginView
from django.views.generic import TemplateView

#ログイン機能
class LoginView(AuthLoginView):
    template_name = 'flaghunt_score/login.html'


class index(TemplateView):
    template_name = "flaghunt_score/index.html"