from django.shortcuts import render, get_object_or_404
from .models import Project


def home(request):
    return render(request, 'portfolio/home.html')


def projects(request):
    project_list = Project.objects.all()

    return render(
        request,
        'portfolio/projects.html',
        {'projects': project_list}
    )


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)

    return render(
        request,
        'portfolio/project_detail.html',
        {'project': project}
    )


def about(request):
    return render(request, 'portfolio/about.html')