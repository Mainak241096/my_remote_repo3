from django.shortcuts import render
import datetime
from django.http import HttpResponse
# Create your views here.
def time_info_view(request):
    time=datetime.datetime.now()
    print(type(time))
    s='<h1>Hello current date and time:'+str(time)+'</h1>'
    return HttpResponse(s)
