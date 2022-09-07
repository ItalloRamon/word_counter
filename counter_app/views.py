from django.shortcuts import render
from django.http import HttpResponse

def count_words(text):
    return len(text.split())

def count_letters(text):
    amount_of_letters = 0
    for letter in text: #Count letter if its different from space and number
        if letter != ' ' and letter not in '1234567890':
            amount_of_letters += 1
    return amount_of_letters

def count_spaces(text):
    amount_of_spaces = 0
    for space in text:
        if space == ' ':
            amount_of_spaces += 1
    return amount_of_spaces

def count_special_chars(text):
    special_characters = '"!@#$%^&*()-+?_=,<>/"'
    amount_special_chars = 0
    for sc in text:
        if sc in special_characters:
            amount_special_chars += 1
    return amount_special_chars

# Create your views here.
def index(request):
    return render(request, 'index.html')

def counter(request):
    text = request.GET['text']
    counter_words = count_words(text)
    counter_letters = count_letters(text)
    counter_spaces = count_spaces(text)
    counter_special_chars = count_special_chars(text)
    context = {
        'words': counter_words,
        'letters': counter_letters,
        'spaces': counter_spaces,
        'specials': counter_special_chars
    }
    return render(request, 'counter.html', context)