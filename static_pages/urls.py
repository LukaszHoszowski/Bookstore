from django.urls import path
from accounts import views

app_name = 'static_pages'

urlpatterns = [
    path("", views.LogoutView.as_view(), name="logout"),
]
