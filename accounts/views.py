from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

from pprint import pprint

def persona_login(request):
    # pprint('assertion: {}'.format(request.POST['assertion']))
    # pprint('keys of POST: {}'.format(request.POST.keys()))
    user = authenticate(assertion=request.POST['assertion'])
    # pprint('user from post: {}'.format(user))
    # pprint('views: email of user: {}'.format(getattr(user, 'email', 'nothing')))
    if user:
        login(request, user)
    return HttpResponse('OK')
