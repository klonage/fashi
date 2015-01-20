from django.http import HttpResponse
from core.models import UserInfo, Style, Gender

# Create your views here.


def assistant_indesx(request):
    return HttpResponse("hej")
