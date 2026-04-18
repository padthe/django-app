from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Message
import json 
from django.views.decorators.csrf import csrf_exempt

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

def get_message_by_id(request, id):
    try:
        message = Message.objects.get(id= id)
    except Message.DoesNotExist:
        return JsonResponse({"error": "message not found"}, status = 404)

    return JsonResponse({
        "id": message.id,
        "text": message.text
    })    

@csrf_exempt
def create_message(request):
    if request.method == "POST":
        body = json.loads(request.body)

        text = body.get("text")
        if not text:
            return JsonResponse({"error": "text is required"}, status = 400)

        message = Message.objects.create(text = text)

        return JsonResponse({
            "id": message.id,
            "text": message.text
        })
    
@csrf_exempt
def delete_message(request,id):
    if request.method == "DELETE":
        try:
            message = Message.objects.get(id=id)
        except Message.DoesNotExist:
            return JsonResponse({"Error:":"Message not found"}, status = 404)
        
        message.delete()

        return JsonResponse({"message":"deleted sucecssfuyllt"})
    
    return JsonResponse({"error": "invalid method"}, status=405)


@csrf_exempt
def message_detail(request, id):
    try:
        message = Message.objects.get(id=id)
    except Message.DoesNotExist:
        return JsonResponse({"error": "Message not found"}, status=404)

    if request.method == "GET":
        return JsonResponse({
            "id": message.id,
            "text": message.text
        })

    elif request.method == "DELETE":
        message.delete()
        return JsonResponse({"message": "Deleted successfully"})

    return JsonResponse({"error": "Invalid method"}, status=405)