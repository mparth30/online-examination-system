from django.db import models
from django.conf import settings
from exams.models import Exam
from questions.models import Question

class Result(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    total_marks = models.IntegerField()
    scored = models.IntegerField()
    taken_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.student.username} - {self.exam.title} - {self.scored}/{self.total_marks}"

class Answer(models.Model):
    result = models.ForeignKey(Result, on_delete=models.CASCADE, null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected = models.CharField(max_length=2, blank=True)
    def __str__(self):
        return f"{self.question.id} -> {self.selected}"
