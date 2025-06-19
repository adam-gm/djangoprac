from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome. You're in the home page.")