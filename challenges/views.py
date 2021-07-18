from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
    "january": "Eat no meat!",
    "february": "Run everyday for 20min!",
    "march": "Learn Django for 20min every day!",
    "april": "Eat no meat!",
    "may": "Run everyday for 20min!",
    "june": "Learn Django for 20min every day!",
    "july": "Eat no meat!",
    "august": "Run everyday for 20min!",
    "september": "Learn Django for 20min every day!",
    "october": "Learn Django for 20min every day!",
    "november": "Eat no meat!",
    "december": "Run everyday for 20min!",
}
# Create your views here.


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
        
    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)
