# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from accounts.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.shortcuts import redirect


def home(request):
    return render(request, 'accounts/index.html')

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'accounts/register.html', args)

def profile(request):
    args1 = {'user': request.user}
    return render(request, 'accounts/profile.html', args1)

def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)