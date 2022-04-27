from django.shortcuts import redirect, render
from .forms import TopicForm  
import MainApp

from .models import Topic

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


