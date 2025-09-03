from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from todoapp.models import task

# Create your views here.
def addtask(request):
    tasks=request.POST['task']
    task.objects.create(tasks=tasks)
    return redirect('home')
def mark_as_done(request,pk):
    tk=get_object_or_404(task,pk=pk)
    tk.is_completed=True
    tk.save()
    return redirect('home')
def delete_task(request,pk):
    tk=get_object_or_404(task,pk=pk)
    tk.delete()
    return redirect('home')
   
def undone_task(request,pk):
    tk=get_object_or_404(task,pk=pk)
    tk.is_completed=False
    tk.save()
    return redirect('home')
def edit_task(request,pk):
    get_task=get_object_or_404(task,pk=pk)
    if request.method=='POST':
        new_task=request.POST['task']
        get_task.tasks=new_task
        get_task.save()
        return redirect('home')
    else:
        context={'get_task':get_task}

    return render(request,'edit_task.html',context)
    get_task=get_object_or_404
 
    """tk=get_object_or_404(task,pk=pk)
    if request.method=='POST':
        tasks=request.POST['task']
        tk.tasks=tasks
        tk.save()
        return redirect('home')
    context={'tk':tk}
    return render(request,'edit.html',context)"""


