from django.shortcuts import render
from .models import Question

def list_questions(request):
    qs = Question.objects.all()
    return render(request, 'questions/list.html', {'questions': qs})
