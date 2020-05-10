#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B.S.D.
Created on Sun May 10 13:15:47 2020
@author: Sara Ben Shabbat
"""

from django.http import HttpResponse
import datetime

def index(request) -> None:
    utc_iso = datetime.datetime.now().isoformat()
    return HttpResponse("Hello, world. You're at polls index. Now is {}".format(utc_iso))


