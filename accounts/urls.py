from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path("logout2/", views.LogoutView.as_view(), name="logout2"),
    # path("signup/", views.SignupPageView.as_view(), name="signup"),
]
