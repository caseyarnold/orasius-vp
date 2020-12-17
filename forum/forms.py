from django import forms
from .models import ForumCategory
from django.core.validators import MinValueValidator

class CreateTopicForm(forms.Form):
    category = forms.ModelChoiceField(queryset=ForumCategory.objects.all())
    title = forms.CharField(label='Title', max_length=100,validators=[MinValueValidator(5)])
    body = forms.CharField(widget=forms.Textarea,label='Body',max_length=1200,validators=[MinValueValidator(20)]
)

class CreateReplyForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea,max_length=1200,validators=[MinValueValidator(20)])