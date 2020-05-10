#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B.S.D.
Created on Sun May 10 13:28:47 2020
@author: Sara Ben Shabbat
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]


