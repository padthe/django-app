from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Message, Booking
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
def message_detail(request,id):
    try:
        message = Message.objects.get(id=id)
    except Message.DoesNotExist:
        return JsonResponse({"error" : "No message was found"}, status = 404)

    if request.method == "GET":
        return JsonResponse({
            "id" : message.id,
            "message" : message.text
        })
    
    elif request.method == "DELETE":
        message.delete()
        return JsonResponse({"message" :"deleted"})
    
    elif request.method == "PUT":
        try:
            body = json.loads(request.body)
        except:
            return JsonResponse({"error" : "Invalid json"})
        
        update_text = body.get("text")

        if not update_text:
            return JsonResponse({"Error" : "text is required"}, status = 400)

    message.text = update_text
    message.save()

    return JsonResponse({
        "id" : message.id,
        "text" : message.text
    })

    
    
@csrf_exempt
def create_booking(request):
    if request.method == "POST":
        body = json.loads(request.body)

        required_fields = ["name", "date", "time"]
        missing_fields = []

        for field in required_fields:
            value = body.get(field)
            if not value:
                missing_fields.append(field)

        if missing_fields:
            return JsonResponse({
                "error" : "missing required field",
                "missing" : missing_fields
            })
        
        booking = Booking.objects.create(
            name = body.get("name"),
            date = body.get("date"),
            time = body.get("time")
        )

        return JsonResponse({
            "id" : booking.id,
            "date" : booking.date,
            "time" : booking.time
        })
    
    return JsonResponse({"error" : "ivalid method"}, status = 405)