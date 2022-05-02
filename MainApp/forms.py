from django import forms

from .models import Entry, Topic

class TopicForm(forms.ModelForm):
    #We are using Meta because we already have a model called forms which are already defined
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}

class EntryForm(forms.ModelForm):
    #We are using Meta because we already have a model called forms which are already defined
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}
        