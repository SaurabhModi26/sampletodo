from django.shortcuts import render
from home.models import Task

# Create your views here.
def index(request):
    if request.method == "POST":
        tasktitle = request.POST['title']
        taskdesc = request.POST['desc']
        print(tasktitle, taskdesc)
        obj = Task(TaskTitle = tasktitle, TaskDesc = taskdesc)
        obj.save()
        
    return render(request,"index.html")
    
def task(request):
    alltasks = Task.objects.all()
    context = {'tasks': alltasks}
    return render(request, "tasklist.html", context)