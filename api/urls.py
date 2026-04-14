from django.urls import path
from .views import hello, get_messages

urlpatterns = [
    path('hello/', hello),
    path('messages/', get_messages)
]