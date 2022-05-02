from django.shortcuts import redirect, render
from .forms import EntryForm, TopicForm  
import MainApp

from .models import Topic, Entry

# Create your views here.

#what type of object is context: dictionary
#Passes information from the view to use in the template (multiple objects needed to be passed, key, value)

#Homepage
def index(request):
    return render(request, 'MainApp/index.html')

def topics(request):
    topics = Topic.objects.order_by('-date_added')
    #topics = Topic.objects.all
    

    #key is what you have to refer to in html
    context={'topics':topics}

    return render(request, 'MainApp/topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.all()

    context = {'topic':topic,'entries':entries}

    #There are 2 types of requests, get and post *KNOW THIS* from slides
    #get request uses it for blank forms
    #post request puts it on the data base
    return render(request, 'MainApp/topic.html', context)

def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()

    else:
        form = TopicForm(data=request.POST)

        if form.is_valid():
            new_topic = form.save()

            return redirect('MainApp:topics')


    context = {'form':form}
    return render(request, 'MainApp/new_topic.html', context)

def new_entry(request,topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()

    else:
        form = EntryForm(data=request.POST)

        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('MainApp:topic',topic_id=topic_id)

    context = {'form':form, 'topic':topic}
    return render(request, 'MainApp/new_entry.html', context)


def edit_entry(request,entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method != 'POST':
        form = EntryForm(instance=entry)

    else:
        form = EntryForm(instance=entry,data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('MainApp:topic',topic_id=topic.id)

    context = {'form':form, 'topic':topic, 'entry':entry}
    return render(request, 'MainApp/edit_entry.html', context)
