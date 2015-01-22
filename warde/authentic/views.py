import calendar

from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from core.models import UserInfo, Style, Gender, UserStyleTemp, ClothesItem, ItemType, Picture
from random import randint
from django.db.models import Q

# Create your views here.
import time


def get_random_object(user):
    return ClothesItem.objects.filter(gender=user.gender, display=True).order_by('?')[0]


def nope(request, h):

    return index(request)

def buy(request, h):
    it = ClothesItem.objects.get(id=h)
    UserInfo.objects.get(user=request.user).bought_clothes.add(it)
    it.display = False
    it.save()

    return index(request)


def have(request, h):
    return buy(request, h)


def wassimilar(request, h):
    return index(request, h, True)


def wasmatch(request, h):
    return index(request, h, False)


def index(request, id=-1, direction=False):
    if request.user.is_authenticated():
        us = UserInfo.objects.get(user=request.user)

        if id == -1:
            item = get_random_object(UserInfo.objects.get(user=request.user))
        elif direction:
            ci = ClothesItem.objects.get(id=id)
            item = \
                ClothesItem.objects.filter(gender=us.gender, style=ci.style, type=ci.type, display=True).order_by('?')[
                    0]
        elif not direction:
            ci = ClothesItem.objects.get(id=id)
            item = \
                ClothesItem.objects.filter(gender=us.gender, style=ci.style).filter(~Q(type=ci.type), display=True).order_by(
                    '?')[0]
        template = loader.get_template('core/main_core.html')

        something = 1 if randint(0, 2) > 1 else 2

        if something == 2:
            cth = us.bought_clothes.all().filter(type=item.type, style=item.style)
        else:
            cth = us.bought_clothes.all().filter(~Q(type=item.type), style=item.style)

        t = min(cth.count(), randint(0, 5))

        if t == 0:
            something = 3

        context = RequestContext(request, {'selected_item': item, 'cnts': cth.order_by(
            '?')[:t], 'something': something})
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
            sval = request.POST.get("ps" + s.name, None)
            UserStyleTemp.objects.create(style=s, value=float(sval) / 10.0, userinfo=newuser)

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
    tab = [
    ]
    for test in tab:
        s = Style.objects.get(id=test[0])
        g = Gender.objects.get(id=test[1])
        t = ItemType.objects.get(id=test[2])
        fname = str(test[3]).split('/')[-1:][0]
        price = 0 if len(test[6]) == 0 else float(test[6].replace(',', '.'))
        ci = ClothesItem.objects.create(type=t, gender=g, style=s, description=test[4], itemname=test[5], price=price,
                                        address='http://google.pl', color=0)
        ci.save()
        ci.images.add(Picture.objects.create(address=fname))

    return HttpResponse('ok')
    # str(s) + ' ' + str(g) + ' ' + str(t) + ' ' + fname + ' ' + str(float(test[6].replace(',', '.'))))


def archive(request):
    us = UserInfo.objects.get(user=request.user)
    context = RequestContext(request, {'request': request, 'user': request.user,
                                       'matches': [val for val in us.bought_clothes.all()]})
    return render_to_response('authentic/archive.html', {}, context_instance=context)
