from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages
from .models import User
from django.http import HttpResponse


def login_message_required(function):
    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.info(request, "로그인한 사용자만 이용할 수 있습니다.")
            return redirect(settings.LOGIN_URL)
    
        return function(request, *args, **kwargs)

    return wrap


def admin_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.level == '1' or request.user.level == '0':
            return function(request, *args, **kwargs)

        messages.info(request, "접근 권한이 없습니다.")
        return redirect('/')

    return wrap


def logout_message_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "접속중인 사용자입니다.")
            return redirect('/')

        return function(request, *args, **kwargs)

    return wrap

def subscribe_message_required(function):
    def wrap(request, *args, **kwargs):
        if (not request.user.is_authenticated):
            messages.info(request, "로그인한 사용자만 이용할 수 있습니다.")
            return redirect(settings.LOGIN_URL)
        elif (request.user.subscribe == '0'):
            messages.info(request, "구독한 사용자만 이용할 수 있습니다.")
            return redirect(settings.SUBSCRIBE_URL)

        return function(request, *args, **kwargs)

    return wrap

def unsubscribe_message_required(function):
    def wrap(request, *args, **kwargs):
        if (not request.user.is_authenticated):
            messages.info(request, "로그인한 사용자만 이용할 수 있습니다.")
            return redirect(settings.LOGIN_URL)
        elif (request.user.subscribe == '1'):
            messages.info(request, "이미 구독 중인 사용자입니다.")
            return redirect('/')

        return function(request, *args, **kwargs)

    return wrap