from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Result

@login_required
def my_results(request):
    qs = Result.objects.filter(student=request.user)
    return render(request, 'results/my.html', {'results': qs})
