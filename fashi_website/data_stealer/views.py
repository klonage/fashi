from django.http import HttpResponse
from data_stealer import models
from django.core import serializers


def index(request):
    return HttpResponse(serializers.serialize('json', models.Clothes.objects.all()))