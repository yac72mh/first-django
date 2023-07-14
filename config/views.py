from django.http import HttpResponse

def home(requst):
    return HttpResponse("hello django")

def abaut(requst):
    return HttpResponse("abaut django")

def contact(requst):
    return HttpResponse("cantact django")