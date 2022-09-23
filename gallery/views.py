from django.shortcuts import render, HttpResponse
import json
# Create your views here.


def gallery(request):
    context = {
        "title": "Gallery"
    }
    return render(request, "gallery/home.html", context=context)
