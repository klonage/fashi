import calendar

from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from core.models import UserInfo, Style, Gender, UserStyleTemp

# Create your views here.
import time


def index(request):
    if request.user.is_authenticated():
        template = loader.get_template('core/main_core.html')
    else:
        template = loader.get_template('authentic/main.html')

    context = RequestContext(request, {'genders': Gender.objects.all, 'preferredstyles': Style.objects.all})
    return HttpResponse(template.render(context))


def secret_login(request):
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    user = authenticate(username=username, password=password)
    if user is not None:
        request.session.set_expiry(0)
        login(request, user)
        return redirect('/')
    if request.user.is_authenticated():
        template = loader.get_template('core/main_core.html')
    else:
        template = loader.get_template('authentic/secret_login.html')

    context = RequestContext(request)
    return HttpResponse(template.render(context))


def join_and_auth(request):
    context = RequestContext(request, {'request': request, 'user': request.user})
    gender_id = request.POST.get('usergender', None)
    if gender_id is not None:
        username = 'big' + str(calendar.timegm(time.gmtime()))
        password = 'lebowski'
        email = username + password + "@gustek.com"
        user = User.objects.create_user(username, email, password)
        newuser = UserInfo.objects.create(user=user, gender=Gender.objects.get(id=int(gender_id)))

        for s in Style.objects.all():
            sval = request.POST.get("ps"+s.name, None)
            UserStyleTemp.objects.create(style=s, value=float(sval)/10.0, userinfo=newuser)

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                request.session.set_expiry(0)
                login(request, user)
                return redirect('/')
    return render_to_response('authentic/main.html', {}, context_instance=context)


def logout_auth(request):
    logout(request)
    return redirect('/')


def algotest(request):
    info = UserInfo.objects.get(user=request.user)
    return HttpResponse(info.gender)