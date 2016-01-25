from django.http import HttpResponse
from django.conf import settings

def home_page(request):
    return HttpResponse('<html><title>To-Do lists</title><body>{}</body></html>'.format(settings.SECRET_KEY))
    #return HttpResponse('<html><title>To-Do lists</title></html>')
