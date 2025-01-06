
from django.http import HttpResponse


def home(response):
    return HttpResponse("hello world , this is from blog app views")