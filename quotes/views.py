import random

from django.shortcuts import render

QUOTES = [
    "Try to be a rainbow in someone else's cloud.",
    "Nothing will work unless you do.",
    "If you don't like something, change it. If you can't change it, change your attitude.",
]

IMAGES = [
    "https://upload.wikimedia.org/wikipedia/commons/b/b4/Maya_Angelou_1989.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/6/64/Maya_Angelou_at_Saving_Our_Sons_2007_%28cropped%29.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/7/7d/Maya_Angelou_cropped_2007_%28brightened%29.jpg",
]


def quote(request):
    context = {
        "quote": random.choice(QUOTES),
        "image_url": random.choice(IMAGES),
    }
    return render(request, "quotes/quote.html", context)


def show_all(request):
    context = {
        "quotes": QUOTES,
        "images": IMAGES,
    }
    return render(request, "quotes/show_all.html", context)


def about(request):
    return render(request, "quotes/about.html")
