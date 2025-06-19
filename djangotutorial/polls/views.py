from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def index(response):
    timeNow = datetime.datetime.now()
    return HttpResponse(f"Welcome. This is the polls page. <br> Current time is: {timeNow}")