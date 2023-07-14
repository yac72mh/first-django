from django.shortcuts import render


def home(requst):
    return render(requst,'root/index.html')

def abaut(requst):
    return render(requst ,"root/abaut.html")

def contact(requst):
    return render(requst , "root/contact.html")