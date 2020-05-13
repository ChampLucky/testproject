# this file is created by me

from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    return render(request, 'index.html')


def removepunc(request):
    text = request.POST.get('text', 'default')
    punc = request.POST.get('punc', 'off')
    newlineremoved = request.POST.get('newline', 'off')
    caps = request.POST.get('caps', 'off')
    punctuations = '''!@#$%^&*()?><":;'>,./\][|}{'''
    analyzed = ""
    NEWLINE = '\n'
    if punc == "on":
        for char in text:

            if char not in punctuations:
                analyzed = analyzed + char

    else:
        analyzed = text

    withnewlineremove = ""
    if newlineremoved == "on":
        for char in analyzed:
            if char != "\n" and char != "\r":
                withnewlineremove = withnewlineremove + char
    else:
        withnewlineremove = analyzed

    final = ""
    if caps == "on":
        for char in withnewlineremove:
            final = final + char.upper()
    else:
        final = withnewlineremove
    dict1 = {'text': final, 'punc': punc}

    return render(request, 'removepunc.html', dict1)
