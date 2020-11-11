from django import forms
from .models import *
import datetime
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class AnnouncementForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Announcement
        fields = ('title','message')


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)
