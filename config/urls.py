import debug_toolbar
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path("", include('static_pages.urls')),
    path("", include('home.urls')),
    path("books/", include('books.urls')),
    path("accounts/", include('allauth.urls')),
    path("accounts/", include('accounts.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]
