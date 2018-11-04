from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from friend.models import Friend

# Create your views here.
def home (request):

    args = dict()
    return render(request, 'homePage/homePage.html', args)
