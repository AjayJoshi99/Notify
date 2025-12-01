from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Notice
from core.decorators import role_required
from .form import NoticeForm

@login_required
def notice_list(request):
    notices = Notice.objects.all().order_by('-created_at')
    return render(request, 'notice_list.html', {'notices': notices})


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
    if request.user.profile.role != "teacher":
        return redirect('notice_list')

    notice = get_object_or_404(Notice, id=id)
    notice.delete()
    return redirect('notice_list')
