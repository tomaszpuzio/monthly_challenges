from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def january(request):
    return HttpResponse("Eat no meet for entire month!")

def february(request):
    return HttpResponse("Walk for at least 20 minutes every day!")

def monthly_challenge(request, month):
    challenge_text = None
    
    if month == "january":
        challenge_text = "Eat no meat!"
    elif month == "february":
        challenge_text = "Run everyday for 20min!"
    elif month == "march":
        challenge_text = "Learn Django for 20min every day!"
    else:
        return HttpResponseNotFound("This month is not supported!")

    return HttpResponse(challenge_text)