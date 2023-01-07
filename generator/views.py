from django.shortcuts import render
from django.http import HttpResponse
import random
import string
import secrets

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')


def password(request):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    try:    
        characters = list()

        if request.GET.get('uppercase'):
            upper_letters = [x.upper() for x in letters]
            characters.extend(list(upper_letters))
        
        if request.GET.get('lowercase'):
            lower_letters = [x.lower() for x in letters]
            characters.extend(list(lower_letters))    

        if request.GET.get('special'):
            characters.extend(list(special_chars))
        
        if request.GET.get('numbers'):
            characters.extend(list(digits))

        length = int(request.GET.get('length', 5))

        thepassword = ''
        
        for x in range(length):
            thepassword += secrets.choice(characters)
    except:
        thepassword = 'ERROR: Select an option to generate password'


    return render(request, 'generator/password.html', {'password': thepassword})

def about(request): 

    return render(request, 'generator/about.html')