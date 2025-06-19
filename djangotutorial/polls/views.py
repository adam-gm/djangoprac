from django.shortcuts import get_object_or_404,render
from django.template import loader
from django.http import HttpResponse
import datetime
from .models import Question
from django.http import Http404

# Create your views here.
def index(request):
    #timeNow = datetime.datetime.now()
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    #template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)
    #return HttpResponse(template.render(context, request))
    #output = ", ".join([q.question_text for q in latest_question_list])
    #return HttpResponse(f"Welcome. This is the polls page. <br> Current time is: {timeNow}. <br> here are the last questions: {output}")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)