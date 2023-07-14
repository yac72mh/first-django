from django.shortcuts import render


def home(requst):
    return render(requst,'index.html')

#def abaut(requst):
#    return render("abaut django")

#def contact(requst):
#    return render("cantact django")