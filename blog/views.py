from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#data

posts = [


    {
        "author":"CoreyMS",
        "title":"Blog Post 1",
        "content":"First post content",
        "date_posted":"Oct 3, 2024"
    },
    {
        "author":"CoreyMS",
        "title":"Blog Post 2",
        "content":"Second post content",
        "date_posted":"Oct 3, 2024"
    }
]

def home(request):
    context = {


        'posts':posts
    }
    return render(request , 'blog/home.html',context) 

def about(request):
    return render(request,'blog/about.html',{'title':"Blog-About"})