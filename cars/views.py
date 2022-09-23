from django.shortcuts import render, HttpResponse
import json
# Create your views here.


def cars(request, car):
    context = {
        "title": "Cars-WeddingCarRide"
    }
    
    if car == "bentley":
        context["car"] = "Bentley"
        context["imgs"] = ["pic1.jpeg", "pic2.jpeg", "pic3.jpeg"]

    return render(request, "cars/home.html", context=context)
