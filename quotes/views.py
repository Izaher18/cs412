import random

from django.shortcuts import render

# Collection of powerful Malcolm X quotes about education, freedom, and justice
QUOTES = [
    "Education is the passport to the future, for tomorrow belongs to those who prepare for it today.",
    "If you don't stand for something you will fall for anything.",
    "The future belongs to those who prepare for it today.",
    "You can't separate peace from freedom because no one can be at peace unless he has his freedom.",
    "I believe in human beings, and that all human beings should be respected as such, regardless of their color.",
]

# Historical images of Malcolm X from local static files
IMAGES = [
    "/static/quotes/images/malcom1.jpg",
    "/static/quotes/images/malcom2.jpg",
    "/static/quotes/images/malcom3.jpg",
]


# View function to display a random Malcolm X quote with a random image
def quote(request):
    context = {
        "quote": random.choice(QUOTES),
        "image_url": random.choice(IMAGES),
    }
    return render(request, "quotes/quote.html", context)


# View function to display all quotes and all images on one page
def show_all(request):
    context = {
        "quotes": QUOTES,
        "images": IMAGES,
    }
    return render(request, "quotes/show_all.html", context)


# View function to display the about page with information about Malcolm X
def about(request):
    return render(request, "quotes/about.html")
