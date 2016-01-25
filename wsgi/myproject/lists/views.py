from datetime import datetime
from django.http import HttpResponse
from django.conf import settings

now = "{:%B %d, %Y}".format(datetime.now())

def home_page(request):
    '''Comments here'''
    return HttpResponse('<html><title>To-Do lists</title><body><div>{}</div><div>{}</div></body></html>'.format('''<pre>boo hoo\n
    whoo hooo</pre>''', now))
    #return HttpResponse('<html><title>To-Do lists</title></html>')
