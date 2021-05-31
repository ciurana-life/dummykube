from django.urls import path
from django.http import HttpResponse

urlpatterns = [path("", lambda _: HttpResponse("Hello world!"))]
