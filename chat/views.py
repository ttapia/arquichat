from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator
from django.urls import reverse


import requests
from .models import Message

def landing(request):
    request.session['username'] = ''
    context = {}
    return render(request, 'chat/landing.html', context)

def index(request):
    latest_message_list = Message.objects.order_by('-pub_date')[:100]
    latest_message_paginator = Paginator(latest_message_list, 5)

    page = request.GET.get('page')
    messages = latest_message_paginator.get_page(page)
    context = { 'messages': messages }

    return render(request, 'chat/index.html', context)

def login(request):
    request.session['username'] = request.POST['username']
    return HttpResponseRedirect(reverse('chat:index'))

def logout(request):
    request.session['username'] = ''
    return HttpResponseRedirect(reverse('chat:landing'))

def send(request):
    new_message = Message(author=request.session['username'], text=request.POST['messageText'])
    new_message.save()
    return HttpResponseRedirect(reverse('chat:index'))

def sendRandomFact(request):
    randomFact = getRandomFact()
    new_message = Message(author=request.session['username'], text=randomFact)
    new_message.save()
    return HttpResponseRedirect(reverse('chat:index'))

def getRandomFact():
    response = requests.get('https://uselessfacts.jsph.pl/random.json?language=en').json()
    return response['text']
