from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Notice
from core.decorators import role_required
from .form import NoticeForm

@login_required
def notice_list(request):
    notices = Notice.objects.filter(created_by=request.user).order_by('-created_at')
    return render(request, "notice_list.html", {"notices": notices})

@login_required
def notice_public(request):
    notices = Notice.objects.all().order_by('-created_at')
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

@role_required("teacher")
def notice_edit(request, id):
    return HttpResponse("Edit page under construction")

@login_required
@role_required("teacher")
def notice_delete(request, id):
    notice = get_object_or_404(Notice, id=id)

    if notice.created_by != request.user:
        return HttpResponse("Unauthorized", status=403)

    notice.delete()
    return redirect("notice_list")