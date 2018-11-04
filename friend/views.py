from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Friend
from django.urls import reverse
from django.http import HttpResponseRedirect


def add_or_remove_friend(request, operation, pk):
    username = User.objects.get(pk=pk)
    friend = User.objects.get(pk=pk)
    if operation=='add':
        Friend.add_friend(request.user, friend)
    elif operation=='remove':
        Friend.remove_friend(request.user, friend)
    return HttpResponseRedirect(reverse('user_page', args=[username]))
