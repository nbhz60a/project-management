from django.shortcuts import render, get_object_or_404
from .models import Project, Task

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
    """
    View to show details of a single project and its tasks.
    """
    project = get_object_or_404(Project, pk=project_id)
    tasks = project.tasks.all() # Using the related_name from the Task model
    context = {
        'project': project,
        'tasks': tasks
    }
    return render(request, 'tracker/project_detail.html', context)
