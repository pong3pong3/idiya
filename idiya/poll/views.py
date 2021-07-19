from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello, customer. You are at the polls index.')
