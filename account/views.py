from django.shortcuts import render, redirect
from .forms import RegistrationForm, UpdateInfoForm
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from django.contrib.auth import update_session_auth_hash




def register(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/account/login/')
    else:
        form = RegistrationForm
        return render(request, 'account/registerPage.html', dict(form=form))


@login_required
def view_profile(request):
    user = request.user
    args = dict(user=user)
    return render(request, 'account/userProfilePage.html', args)


@login_required
def change_password(request):
    if request.method=='POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return render(request, 'account/changePasswordComplete.html', dict())
    else:
        form = PasswordChangeForm(user=request.user)
        args = dict(form=form)
        return render(request, 'account/changePasswordPage.html', args)


@login_required
def update_info(request):
    if request.method=='POST':
        form = UpdateInfoForm(request.POST, instance=request.user)
        if form.is_valid:
            form.save()
            return redirect('/account/profile')
    else:
        form = UpdateInfoForm(instance=request.user)
        args = dict(form=form)
        return render(request, 'account/updateInfoPage.html', args)




