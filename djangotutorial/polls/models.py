from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
# Basically creates tables in database as a class, and the defined members are columns in the table. Then an instance of the class would be a row
# The class is a child of Djangos Model class


class Question(models.Model):
    def __str__(self):
        return self.question_text
    
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
class Choice(models.Model):
    def __str__(self):
        return self.choice_text
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)