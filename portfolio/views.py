from django.shortcuts import render
from .models import Project, Skill

def portfolio(request):
    projects = Project.objects.all()  # Get all projects
    skills = Skill.objects.all()  # Get all skills
    context = {'projects': projects, 'skills': skills}
    return render(request, 'portfolio/portfolio.html', context)
