from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from accounts.models import UserProfile

def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(f"Received signup data: {first_name}, {last_name}, {email}, {password}")

        user_obj = User.objects.filter(email=email)
        if user_obj.exists():
            messages.warning(request, "Email already exists.")
            return HttpResponseRedirect(request.path_info)
        
        user = User.objects.create_user(username=email, first_name=first_name, last_name=last_name, email=email)
        user.set_password(password)
        user.save()
        messages.success(request, "A verification email has been sent to your email address.")
        return HttpResponseRedirect(request.path_info)
            
    return render(request, 'accounts/signup.html')


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        user_obj = User.objects.filter(username=email)

        if not user_obj.exists():
            messages.warning(request, "Account not found!!!")
            return HttpResponseRedirect(request.path_info)
        
        if not user_obj[0].profile.is_email_verified:
            messages.warning(request, "Your account is not verified!!!\nCheck your inbox")
            return HttpResponseRedirect(request.path_info)
        
        authenticated_user = authenticate(request, username=email, password=password)

        if authenticated_user is not None:
            login(request, authenticated_user)
            return redirect("/")
        
        messages.warning(request, "Invalid credidentials!!!")
        return HttpResponseRedirect(request.path_info)


    return render(request, "accounts/login.html")


def logout_page(request):
    logout(request)
    return redirect("/")


def activate_email(request, email_token):
    try:
        user = UserProfile.objects.get(email_token=email_token)
        user.is_email_verified = True
        user.save()
        login(request, user.user)
        messages.success(request, "Your account has been verified successfully!")
    except ObjectDoesNotExist:
        return HttpResponse("Invalid email token")
    
    return redirect("/")
