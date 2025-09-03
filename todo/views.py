from django.shortcuts import render
from todoapp.models import task
def home(request):
    tk=task.objects.filter(is_completed=False).order_by('-created_at')
    completed_tasks=task.objects.filter(is_completed=True)
    
    context={'tk':tk,
             'completed_tasks':completed_tasks}
    print(context)
    return render(request,'home.html',context)