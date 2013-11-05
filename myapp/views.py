# Create your views here.
from django.http import HttpResponse
import datetime
 
def index(request):
    return HttpResponse("Hello, world from the polls App! L33t")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

