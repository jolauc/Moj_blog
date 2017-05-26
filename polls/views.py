from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response

from polls.models import *


def index(request):
    polls = Question.objects.all().order_by('-posted_date')
    return render_to_response('index.html',
            {'polls': polls},
            context_instance=RequestContext(request))
# Create your views here.

# Create your views here.
