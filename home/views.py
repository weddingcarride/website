from django.shortcuts import render, HttpResponse
import json
# Create your views here.


def home(request):
    context = {
        "title": "WeddingCarRide"
    }
    return render(request, "home/home.html", context=context)
