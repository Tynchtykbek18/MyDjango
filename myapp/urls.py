from django.contrib import admin
from django.urls import path
from .views import first_page, thanks_page
urlpatterns = [
    path('', first_page, name='first_page'),
    path('thanks_page/', thanks_page, name='thanks_page')
]
