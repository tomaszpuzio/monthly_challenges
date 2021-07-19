from typing import Reversible
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html")
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
    