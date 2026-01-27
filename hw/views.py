from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

import time
import random

# Create your views here.

def home(requst): 
    '''Funds to respond to the home request.'''
    
    response_text = f'''
    <html>
        <h1>Welcome to HW Home Page</h1>
        <p>This is the home page for the HW app.</p>
        <p>The current time is {time.ctime()}.</p>
    </html>
    '''

    return HttpResponse(response_text)



def home_page(request):
    '''Define a view to show the 'home.html' template.'''

    # the template to which we will delegate the work
    template = 'hw/home.html'

    # a dict of key/value pairs, to be available for use in template
    context = {
        'current_time': time.ctime(),
        'letter1' : chr(random.randint(65,90)),
        'letter2' : chr(random.randint(65,90)),
        'number' : random.randint(1,10),
    } 

    return render(request, template, context)