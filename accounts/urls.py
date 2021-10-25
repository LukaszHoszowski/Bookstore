from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path("", views.LogoutView.as_view(), name="logout"),
    path("signup/", views.SignupPageView.as_view(), name="signup"),
]
