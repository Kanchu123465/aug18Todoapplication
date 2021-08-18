from django.shortcuts import render

# Create your views here.

from todo.models import Todo
from todo.serialize import TodoSerializers
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

@csrf_exempt
def My_details(request):
    if(request.method=="GET"):
        todos=Todo.objects.all()
        todo_serializer=TodoSerializers(todos,many=True)
        return JsonResponse(todo_serializer.data,safe=False)



@csrf_exempt
def MyaddPage(request):
    if (request.method=="POST"):
        mydata=JSONParser().parse(request)
        todo_data=TodoSerializers(data=mydata)
        if(todo_data.is_valid()):
            todo_data.save()
            return JsonResponse(todo_data.data)
        else:
            return HttpResponse("error in Serialization")
    else:
        return HttpResponse("No get method is allowed")

@csrf_exempt
def singleview(request,id):
    try:
        todo = Todo.objects.get(id = id)
        if(request.method == "GET"):
            todo_serializer = TodoSerializers(todo)
            return JsonResponse(todo_serializer.data,safe=False)




    except Todo.DoesNotExist:
        return HttpResponse("Invalid ID")
