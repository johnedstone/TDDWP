from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render

def persona_login(request):
    authenticate(assertion=request.POST['assertion'])
    return HttpResponse()
