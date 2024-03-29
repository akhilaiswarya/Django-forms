from django import forms
from app.models import *

class TopicForm(forms.Form):
    topic_name=forms.CharField()

class WebPageForm(forms.Form):
    tl=[[to.topic_name,to.topic_name] for to in Topic.objects.all()]
    topic_name=forms.ChoiceField(choices=tl)
    name=forms.CharField()
    url=forms.URLField()
    gmail=forms.EmailField()

class AccessRecordForm(forms.Form):
    wl=[[wo.pk,wo.name] for wo in WebPage.objects.all()]
    name=forms.ChoiceField(choices=wl)
    date=forms.DateField()
    author=forms.CharField()




