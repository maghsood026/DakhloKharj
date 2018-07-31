# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse, HttpResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from .models import Income, Expense, Token, User
from datetime import datetime
from django.shortcuts import render


@csrf_exempt
def submit_expense(request):
    print(request.POST)
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()
    Expense.objects.create(text=request.POST['text'], user=this_user, amount=request.POST['amount'], time=date)

    return JsonResponse({
        'status': 'Ok',
    }, encoder=JSONEncoder)


@csrf_exempt
def submit_income(request):
    print(request.POST)
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()
    Income.objects.create(text=request.POST['text'], user=this_user, amount=request.POST['amount'], time=date)

    return JsonResponse({
        'status': 'Ok',
    }, encoder=JSONEncoder)


def edit(request):
    return HttpResponse("<h1>Edit page ...</h1>")
