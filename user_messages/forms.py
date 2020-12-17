from django import forms
from .models import UserMessage
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

class CreateUserMessageForm(forms.Form):
    class Meta:
        model = User

    def user_exists(self):
        username = self.cleaned_data.get('to_user')
        if User.objects().get(username=username).count() != 1:
            raise forms.ValidationError(u'This user does not exist!')
        elif User.objects().get(username=username).is_banned == True:
            raise forms.ValidationError(u'This user has been banned')
        return username

    to_user = forms.CharField(label='To', validators=[MinValueValidator(3)])
    title = forms.CharField(label='Title', max_length=100,validators=[MinValueValidator(5)])
    body = forms.CharField(widget=forms.Textarea,label='Body',max_length=1200,validators=[MinValueValidator(20)])