'''
Common views of the website
'''

from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def page_not_found(request, exception):
    return render(request, '404.html', {})
