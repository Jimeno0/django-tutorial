from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse, Http404

from .models import Question 

def index(request):
  latest_questions_list = Question.objects.order_by('-date_published')[:5]
  context = {
    'latest_questions_list' : latest_questions_list,
  }
  return render(request, 'polls/index.html', context)
  

def details (request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request,'polls/details.html', {'question':question})


def result(request, question_id):
  return HttpResponse(' You are at the results page for question id %s' % question_id)
def vote(request,question_id):
  return HttpResponse('You are at the vote page for question id %s' % question_id)



