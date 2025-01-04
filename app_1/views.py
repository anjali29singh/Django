from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return HttpResponse("hello world , this is from app view")
