from django.db import models
class Question(models.Model):
    text = models.TextField()
    option_a = models.CharField(max_length=300)
    option_b = models.CharField(max_length=300)
    option_c = models.CharField(max_length=300, blank=True)
    option_d = models.CharField(max_length=300, blank=True)
    CORRECT_CHOICES = (('A','A'),('B','B'),('C','C'),('D','D'))
    correct = models.CharField(max_length=1, choices=CORRECT_CHOICES)
    marks = models.IntegerField(default=1)
    def __str__(self):
        return self.text[:50]
