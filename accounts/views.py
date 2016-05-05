from django.shortcuts import render, redirect
from django.contrib.auth import logout


from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)

from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)


# Create your views here.
def login(request):
    c = {}
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            x = auth_login(request, form.get_user())
            return redirect("/")
            # print "_________________________"
            print x
        else:
            # print "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
            # print "BAD USER"

            return redirect("/login_failed/")
    else:
         return render(request, 'registration/login.html', c)


def login_failed(request):
         return render(request, 'registration/login_failed.html', {})

def my_logout(request):
    logout(request)
    return redirect("/")
