from django.urls import path
from .views import my_results
urlpatterns=[path('my/', my_results, name='my_results')]
