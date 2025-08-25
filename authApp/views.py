
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views import View
from .forms import signUp, Login  

class DashboardView(View):
    def get(self, request):
        return render(request, 'dashboard.html')

class SignUpView(View):
    def get(self, request):
        form = signUp()
        return render(request, 'signup.html', {'form': form})
    
    def post(self, request):
        form = signUp(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  
            return redirect("/dashboard")
        return render(request, "signup.html", {"form": form})


class LoginView(View):
    def get(self, request):
        form = Login()
        return render(request, 'login.html', {"form": form})
    
    def post(self, request):
        form = Login(request.POST)
        if form.is_valid():
            login(request, form.get_user) 
            return redirect("/fdashboard")  
        return render(request, "login.html", {"form": form}) 


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("authApp:login")  


