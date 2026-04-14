from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Message

# Create your views here.

def hello(request):
    return HttpResponse("Hello Patrick")

def get_messages(request):
    messages = Message.objects.all()

    data = []
    for msg in messages:
        data.append({
            "id": msg.id,
            "text": msg.text
        })

    return JsonResponse(data, safe= False)