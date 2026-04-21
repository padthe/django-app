from django.urls import path
from .views import hello, get_messages, create_message, message_detail, create_booking

urlpatterns = [
    path('hello/', hello),
    path('messages/', get_messages),
    path('messages/create/', create_message),
    path('messages/<int:id>/', message_detail),
    path('booking/create/', create_booking)
]