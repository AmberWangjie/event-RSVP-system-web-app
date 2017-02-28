from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text




class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self):
        return str(self.username)

class Event(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    owner_name = models.CharField(max_length=50, default="admin")
    title = models.CharField(max_length=50)
    descrption = models.CharField(max_length=200)
    event_time = models.CharField(max_length=50,default="1/1/1970")
    date = models.DateField(auto_now_add=True)
    place = models.CharField(max_length=50)
    plusOne = models.BooleanField(default=False)

class Answer(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    event_title = models.CharField(max_length=50, default="none")
    answered_by = models.ForeignKey(User, on_delete=models.CASCADE)
    answer_name = models.CharField(max_length=100, default="admin")
    comment = models.CharField(max_length=100, default="none")
    data = models.DateField(auto_now_add=True)
    plusOne = models.BooleanField(default=False)
    willCome = models.BooleanField(default=False)
    def __str__(self):
        return str(self.event.title) + " -- " + str(self.answered_by)

class Relationship(models.Model):
    event_title = models.CharField(max_length=50)
    guest_name = models.CharField(max_length=50)
    isAnswered = models.BooleanField(default=False)