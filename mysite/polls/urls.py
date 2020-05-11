#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B.S.D.
Created on Sun May 10 13:28:47 2020
@author: Sara Ben Shabbat
"""

from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote')
]


