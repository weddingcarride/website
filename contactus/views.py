from django.shortcuts import render, HttpResponse
import json
# Create your views here.


def gallery(request):
    context = {
        "title": "ContactUs-WeddingCarRide"
    }
    return render(request, "contactus/home.html", context=context)
