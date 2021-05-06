from django.shortcuts import render
from .models import TodoItems
from django.http import HttpResponseRedirect

def toDoList(request):
    context={
    'data' : TodoItems.objects.all() 
    }
    return render(request,'listArea/home.html',context)

def addtodo(request):
    new_item = TodoItems(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/')

def deltodo(request,todo_id):
   item_to_delete = TodoItems.objects.get(id=todo_id)
   item_to_delete.delete()
   return HttpResponseRedirect('/')
