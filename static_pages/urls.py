from django.urls import path
from static_pages import views

app_name = 'static_pages'

urlpatterns = [
    path("about/", views.AboutView.as_view(), name="about"),
]
