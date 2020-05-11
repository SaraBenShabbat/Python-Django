#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B.S.D.
Created on Sun May 10 13:15:47 2020
@author: Sara Ben Shabbat
"""

from django.http import HttpResponse
from django.shortcuts import get_object_or_404,render

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    
    return render(request, 'polls/index.html', context)


def detail(request, question_id: int) -> HttpResponse: 
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
        

def results(request, question_id: int) -> HttpResponse:
    response = "You're looking at the results of question {}."
    return HttpResponse(response.format(question_id))


def vote(request, question_id: int) -> HttpResponse:
    return HttpResponse("You're voting on question {}.".format(question_id))


