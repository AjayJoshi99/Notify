from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from core.decorators import role_required
from django.contrib.auth.decorators import login_required
from notices.models import Notice 

def home(request):
    return HttpResponse("Home Page Working!")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            role = getattr(user.profile, "role", None)
            if role == "teacher":
                return redirect("teacher_dashboard")
            else:
                return redirect("student_dashboard")

        return redirect("/login?error=1")
    error = "Invalid username or password" if request.GET.get("error") else None
    return render(request, "login.html", {"error": error})


def logout_view(request):
    logout(request)
    
    return redirect("login")

@login_required
@role_required("teacher")
def teacher_dashboard(request):
    notices = Notice.objects.all().order_by('-pinned', '-created_at')
    return render(request, "teacher_dashboard.html", {"notices": notices})

@role_required("student")
def student_dashboard(request):
    return render(request, "student_dashboard.html")
