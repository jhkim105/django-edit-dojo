from django.shortcuts import render

from django.http import HttpResponse

def todoView(request):
    return HttpResponse('hello. this is todo view')