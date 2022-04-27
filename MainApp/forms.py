from django import forms

from .models import Topic

class TopicForm(forms.ModelForm):
    #We are using Meta because we already have a model called forms which are already defined
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}