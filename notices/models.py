from django.db import models
from django.contrib.auth.models import User
from core import models as core

class Notice(models.Model):
    CATEGORY_CHOICES = [
        ("general", "General"),
        ("exam", "Exam"),
        ("holiday", "Holiday"),
        ("event", "Event"),
        ("urgent", "Urgent"),
    ]

    PRIORITY_CHOICES = [
        ("high", "High"),
        ("medium", "Medium"),
        ("low", "Low"),
    ]
    title = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    saved_by = models.ManyToManyField(core.Profile, blank=True, related_name="saved_notices")

    attachment = models.FileField(
        upload_to="notices/",
        blank=True,
        null=True
    )
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="general")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default="medium")
    expiry_date = models.DateField(null=True, blank=True)
    pinned = models.BooleanField(default=False)
   
    
    def is_expired(self):
        from datetime import date
        return self.expiry_date and self.expiry_date < date.today()
    def __str__(self):
        return self.title

class NoticeComment(models.Model):
    notice = models.ForeignKey(Notice, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
