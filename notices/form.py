from django import forms
from .models import Notice

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = [
            "title",
            "message",
            "attachment",
            "category",
            "priority",
            "expiry_date",
            "pinned"
        ]
        widgets = {
            "expiry_date": forms.DateInput(attrs={"type": "date"}),
            "priority": forms.Select(attrs={"class": "form-select"}),
            "category": forms.Select(attrs={"class": "form-select"}),
        }
