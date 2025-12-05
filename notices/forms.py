from django import forms
from .models import NoticeComment 
class CommentForm(forms.ModelForm):
    class Meta:
        model = NoticeComment
        fields = ["comment"]