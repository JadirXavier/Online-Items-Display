from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse
from django.conf import settings
import requests
import logging


# Create your views here.

def index(request):
    return render(request, "mostruario/index.html")