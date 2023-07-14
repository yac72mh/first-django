from django.urls import path , include
from .views import *

urlpatterns = [
    path('' , home),
    path('abaut' , abaut),
    path('contact' , contact)

]