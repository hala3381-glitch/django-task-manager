from django.shortcuts import render, redirect, get_object_or_404
from .models import Goals
# Create your views here.

def main_page(request):
    return render(request,'base.html')



def tracker_page(request, task_id = None):
    task = None
    if task_id:
        task = get_object_or_404(Goals, id = task_id)
    if request.method == 'POST':
        task_title = request.POST.get('goal')
        task_status = request.POST.get('status')
        if task_title:
            if task:
                task.goal = task_title
                task.status = task_status
                task.save()
            else:
                Goals.objects.create(goal=task_title, status=task_status)
            return redirect('trackers')
    return render(request,'tracker/new_tracker.html')

def trackers(request):
    all_objects = Goals.objects.all()
    
    recent_goal = request.session.get('last_added_goal','you did not add any goals recently')
    
    con = {
        'goals_list': all_objects,
    }
    return render(request,'tracker/tasks.html',con )

def delete_task(request, task_id ):
    task = get_object_or_404(Goals, id = task_id)

    task.delete()

    return redirect('trackers')