from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReminderForm, CompletedWorkForm
from .models import Project, Task, Reminder

def reminder_list(request):
    """
    View to list all reminders.
    """
    reminders = Reminder.objects.order_by('date')
    context = {
        'reminders': reminders
    }
    return render(request, 'tracker/reminder_list.html', context)

def project_list(request):
    """
    View to list all projects.
    """
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'tracker/project_list.html', context)

def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    tasks = project.tasks.all()
    reminders = project.reminders.all()

    if request.method == 'POST':
        if 'add_reminder' in request.POST:
            reminder_form = ReminderForm(request.POST)
            if reminder_form.is_valid():
                reminder = reminder_form.save(commit=False)
                reminder.project = project
                reminder.save()
                return redirect('tracker:project_detail', project_id=project.id)
        elif 'upload_work' in request.POST:
            completed_work_form = CompletedWorkForm(request.POST, request.FILES, instance=project)
            if completed_work_form.is_valid():
                completed_work_form.save()
                return redirect('tracker:project_detail', project_id=project.id)
    else:
        reminder_form = ReminderForm()
        completed_work_form = CompletedWorkForm(instance=project)

    context = {
        'project': project,
        'tasks': tasks,
        'reminders': reminders,
        'reminder_form': reminder_form,
        'completed_work_form': completed_work_form,
    }
    return render(request, 'tracker/project_detail.html', context)
