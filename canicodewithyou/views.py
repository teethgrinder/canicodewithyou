# -*- coding: utf-8 -*-
from django.shortcuts import render
 

def home(request):
  context =  {}
  return render(request, "canicodewithyou/index.html", context)