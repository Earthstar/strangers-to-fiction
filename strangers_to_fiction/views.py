from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context
from django.views.defaults import server_error

from webcomic_cms.models import Comic, NewsPost, Comment

def home(request):
    context = {}
    return render(request, 'home.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)

def archive(request):
    if request.method == 'GET':
        comics = Comic.objects.order_by('number').reverse().values()
        context = {'comics': comics}
        return render(request, 'archive.html', context)

def comic(request, number):
    '''
    number - number of the comic to view.
    Returns 500 error if request a comic that isn't visible yet.
    '''
    if request.method == 'GET':
        try:
            comic = Comic.objects.get(number=number)
        except:
            return server_error(request)
        # This works, but it seems inelegant
        context = {'comic':
            {
            'title': comic.title,
            'number': comic.number,
            'image': comic.image,
            'alt_text': comic.alt_text,
            'commentary': comic.commentary,
            'date_posted': comic.date_posted,
            'is_first': comic.is_first(),
            'is_last': comic.is_last(),
        }}
        return render(request, 'comic.html', context)

def first_comic(request):
    '''
    Returns a page with the first visible comic.
    Assumes the first comic is number 1.
    '''
    return comic(request, 1)

def last_comic(request):
    '''
    Returns a page with the last visible comic.
    '''
    # Get the last number
    last_number = Comic.objects.order_by('number').last().number
    return comic(request, last_number)