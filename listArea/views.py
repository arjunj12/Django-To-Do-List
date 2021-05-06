from django.shortcuts import render

def toDoList(request):
    return render(request,'listArea/list.html',{'data': data})