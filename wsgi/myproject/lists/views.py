from django.http import HttpResponse
from django.conf import settings

def home_page(request):
    return HttpResponse('<html><title>To-Do lists</title><body>{}</body></html>'.format('''<pre>boo hoo\n
    whoo hooo</pre>'''))
    #return HttpResponse('<html><title>To-Do lists</title></html>')
