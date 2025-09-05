from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Exam
from results.models import Result, Answer
from questions.models import Question

@login_required
def list_exams(request):
    qs = Exam.objects.filter(active=True)
    return render(request, 'exams/list.html', {'exams': qs})

@login_required
def start_exam(request, pk):
    exam = get_object_or_404(Exam, pk=pk, active=True)
    return render(request, 'exams/take.html', {'exam': exam})

@login_required
def submit_exam(request, pk):
    exam = get_object_or_404(Exam, pk=pk, active=True)
    if request.method == 'POST':
        total_marks = 0
        scored = 0
        res = Result.objects.create(student=request.user, exam=exam, total_marks=0, scored=0)
        for q in exam.questions.all():
            total_marks += q.marks
            selected = request.POST.get(f'question_{q.id}', '')
            Answer.objects.create(result=res, question=q, selected=selected)
            if selected == q.correct:
                scored += q.marks
        res.total_marks = total_marks
        res.scored = scored
        res.save()
        messages.success(request, f'Exam submitted. Score: {scored}/{total_marks}')
        return redirect('my_results')
    return redirect('exams_list')
