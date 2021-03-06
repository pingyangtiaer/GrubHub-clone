# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Grubber, GrubberManager, UserAddress
from time import gmtime, strftime
from django.utils import timezone

def index(request):
    if 'id' in request.session:
        return redirect('users:main_profile')
    return render(request, 'users/index.html')

def login(request):
    gm = GrubberManager()
    valid, response = gm.login_reg_validator(request.POST, 'login')
    if not valid:
        for error in response:
            messages.error(request, error)
        return redirect('users:index')
    request.session['id'] = response
    return redirect("users:lets_eat")

def register(request):
    gm = GrubberManager()
    valid, response = gm.login_reg_validator(request.POST, 'register')
    if not valid:
        for error in response:
            messages.error(request, error)
        return redirect('users:index')
    request.session['id'] = response
    return redirect("users:lets_eat")

def show_profile(request):
    if 'id' in request.session:
        hour = int(strftime("%H", gmtime()))
        hour = (hour - 6) % 24
        if hour >= 18:
            time = 'evening'
        elif hour >= 12:
            time = 'afternoon'
        else:
            time = 'morning'
        if 'id' in request.session:
            user = User.objects.get(id=request.session['id'])
        else:
            user = []
        context = {
            'user': user,
            'time': time
        }
        return render(request, "users/lets-eat.html", context)
    return redirect('users:index')

def show_account(request):
    if 'id' in request.session:
        context = {
            'user': User.objects.get(id=request.session['id'])
        }
        return render(request, "users/account.html", context)
    return redirect('users:index')

def update_name(request):
    response = Grubber.objects.modify_user(request.POST, 'update_name')
    return redirect('users:main_profile')

def update_email(request):
    response = Grubber.objects.modify_user(request.POST, 'update_email')
    return redirect('users:main_profile')

def update_password(request):
    response = Grubber.objects.modify_user(request.POST, 'update_password')
    return redirect('users:main_profile')

def show_addresses(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        'user': user,
        'addresses': user.addresses.all()
    }
    return render(request, "users/address.html", context)

def add_address(request):
    valid, response = UserAddress.objects.address_validator(request.POST)
    if not valid:
        for error in response:
            messages.error(request, error)
        return redirect('users:user_addresses')
    return redirect('users:user_addresses')

def update_address(request):
    response = UserAddress.objects.updated_address(request.POST)
    print response
    return redirect('users:user_addresses')

def destroy_address(request, address_id):
    address_deleting = UserAddress.objects.get(id=address_id)
    address_deleting.delete()
    return redirect('users:user_addresses')

def reset(request):
    request.session.clear()
    return redirect('users:index')
