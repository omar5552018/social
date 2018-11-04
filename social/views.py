from django.shortcuts import redirect
from django.http import HttpResponseRedirect

def redirectToHome(request):
    return HttpResponseRedirect('/home/')