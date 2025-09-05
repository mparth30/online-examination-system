from django.urls import path
from . import views
urlpatterns=[path('list/', views.list_exams, name='exams_list'), path('start/<int:pk>/', views.start_exam, name='start_exam'), path('submit/<int:pk>/', views.submit_exam, name='submit_exam')]
