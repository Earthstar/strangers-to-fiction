from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context

def home(request):
    context = {}
    return render(request, 'home.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)

def archive(request):
    context = {}
    return render(request, 'archive.html', context)

def comic(request):
    context = {}
    return render(request, 'comic.html', context)