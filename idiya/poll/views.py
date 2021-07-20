from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Question

def yandex(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)
    context = {'lql': latest_question_list,}
    return render(request, 'poll/index.html', context) 

def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'poll/detail.html', {'qstn': question})

def results(request, question_id):
    response = 'You are looking at the results of question %s.' 
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse('You are voting on question %s.' % question_id)

