from django.urls import path
from .views import hello, get_messages, create_message, message_detail

urlpatterns = [
    path('hello/', hello),
    path('messages/', get_messages),
    path('create/', create_message),
    path('messages/<int:id>/', message_detail),
]