from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import View
from .models import Subscriber
from .forms import SubscriberForm

def home(request):
    form = SubscriberForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        new_form = form.save()
    return render(request, 'landing/home.html', locals())

def users(request):
    users = Subscriber.objects.all()
    return render(request, 'landing/home_users.html', {'objects_list': users})

class SubscriberDetailView(DetailView):
    queryset = Subscriber.objects.all()
    context_object_name = 'object'
    template_name = 'landing/detail.html'





