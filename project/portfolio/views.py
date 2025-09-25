from django.shortcuts import render, redirect
from .models import Project, Skill
from .forms import ContactMessageForm

def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()

    if request.method == "POST":
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()  # Bazaga saqlaydi
            return redirect("home")  # sahifani yangilaydi
    else:
        form = ContactMessageForm()

    return render(request, "index.html", {
        "projects": projects,
        "skills": skills,
        "form": form
    })

def contact(request):
    if request.method == "POST":
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ContactMessageForm()
    return render(request, "profile.html", {"form": form})
