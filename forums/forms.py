from tkinter import Widget
from django.forms import ModelForm
from .models import Subforum, Thread



class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        fields = '__all__'
        exclude = ['host', 'sticked']
