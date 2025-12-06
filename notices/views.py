from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Notice
from core.decorators import role_required
from .form import NoticeForm
from django.utils import timezone

@login_required
@role_required("teacher")
def notice_list(request):
    notices = (
        Notice.objects.filter(created_by=request.user)
        .order_by('-pinned', '-created_at')
    )
    return render(request, "notice_list.html", {"notices": notices})

@login_required
def notice_public(request):
    today = timezone.now().date()

    notices = (
        Notice.objects.filter(expiry_date__gte=today)  
        .order_by('-pinned', '-created_at')        
    )

    return render(request, 'notice_public.html', {'notices': notices})


@login_required
@role_required("teacher")
def notice_create(request):
    if request.method == "POST":
        form = NoticeForm(request.POST, request.FILES)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.created_by = request.user
            notice.save()
            return redirect("notice_list")
    else:
        form = NoticeForm()

    return render(request, "notice_form.html", {"form": form})


@login_required
@role_required("teacher")
def notice_edit(request, id):
    notice = get_object_or_404(Notice, id=id)

    if notice.created_by != request.user:
        return HttpResponse("Unauthorized", status=403)

    if request.method == "POST":
        form = NoticeForm(request.POST, request.FILES, instance=notice)
        if form.is_valid():
            form.save()
            return redirect("notice_list")

    form = NoticeForm(instance=notice)
    return render(request, "notice_form.html", {"form": form})

@login_required
@role_required("teacher")
def notice_delete(request, id):
    notice = get_object_or_404(Notice, id=id)

    if notice.created_by != request.user:
        return HttpResponse("Unauthorized", status=403)

    notice.delete()
    return redirect("notice_list")

@login_required
def notice_save(request, id):
    notice = get_object_or_404(Notice, id=id)
    profile = request.user.profile  
    if profile in notice.saved_by.all():
        notice.saved_by.remove(profile)  
    else:
        notice.saved_by.add(profile)  
    return redirect("student_dashboard")

@login_required
def notice_saved_list(request):
    profile = request.user.profile
    saved_notices = profile.saved_notices.all()
    return render(request, "notice_saved.html", {"notices": saved_notices})
