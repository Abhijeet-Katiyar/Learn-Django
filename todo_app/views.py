from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import TodoList
# Create your views here.

def todo_view(request,*args,**kwargs):
    task_a=TodoList.objects.all()
    AllTask={'task_a':task_a}
    return render(request,'todo.html',AllTask)

def addtodo(request):
    new_item=TodoList.objects.create(task=request.POST["task"])
    return HttpResponseRedirect('/todo/')

def deletetodo(request,todo_id):
    TodoList.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/todo/')
