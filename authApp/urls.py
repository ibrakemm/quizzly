from django.urls import path
from . import views

app_name = 'authApp'
urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("logout/", views.LogoutView.as_view(), name="Logout"),
    path("", views.DashboardView.as_view(), name="Dashboard")
]


