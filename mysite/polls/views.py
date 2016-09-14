from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse, Http404, HttpResponseRedirect

from .models import Question, Choice

from django.urls import reverse

from django.views import generic

# def index(request):
#   latest_questions_list = Question.objects.order_by('-date_published')[:5]
#   context = {
#     'latest_questions_list' : latest_questions_list,
#   }
#   return render(request, 'polls/index.html', context)

# def details (request, question_id):
#   question = get_object_or_404(Question, pk=question_id)
#   return render(request,'polls/details.html', {'question':question})

# def result(request, question_id):
#   question = get_object_or_404(Question, pk= question_id)

#   return render(request, 'polls/results.html', {'question': question})

class indexView(generic.ListView):
  template_name = 'polls/index.html'
  context_object_name = 'latest_questions_list'

  def get_queryset (self):
    return Question.objects.order_by('-date_published')[:5]

class detailsView(generic.DetailView):
  model = Question
  template_name = 'polls/details.html'

class resultView(generic.DetailView):
  model = Question
  template_name = 'polls/results.html'


def vote(request,question_id):
  question = get_object_or_404(Question, pk = question_id)

  try:
    selected_choice = question.choice_set.get(pk = request.POST['choice'])

  except (KeyError, Question.DoesNotExist):
    return render(request, 'polls/details.html', {'question': question, 'error_messager' : 'You didnt selected any question'})

  else:
    selected_choice.votes += 1
    selected_choice.save()


    return HttpResponseRedirect(reverse('polls:result', args=[question.id]))
    #or:
    #return HttpResponseRedirect(reverse('polls:result', kwargs={'pk': question.id}))
  






