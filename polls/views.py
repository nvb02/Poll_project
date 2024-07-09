from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib import messages

# Create your views here.

def poll_list(request):
    polls = Poll.objects.all()
    return render(request, 'poll_list.html', {'polls': polls})

def poll_detail(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    return render(request, 'poll_detail.html', {'poll': poll})

def vote(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    choice_id = request.POST.get('choice')
    if choice_id:
        choice = get_object_or_404(Choice, id=choice_id)
        Vote.objects.create(poll=poll, choice=choice)
        messages.success(request, 'Your vote has been recorded!')
    else:
        messages.error(request, 'No choice selected.')
    return redirect('poll_detail', poll_id=poll.id)