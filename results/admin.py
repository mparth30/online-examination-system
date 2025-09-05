from django.contrib import admin
from .models import Result, Answer
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('student','exam','scored','total_marks','taken_on')
@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question','selected','result')
