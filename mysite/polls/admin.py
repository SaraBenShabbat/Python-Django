#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B.S.D.
Created on Sun May 10 13:28:47 2020
@author: Sara Ben Shabbat
"""

from django.contrib import admin

from .models import Question

admin.site.register(Question)


