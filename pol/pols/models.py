from django.db import models
from datetime import date



class Polls(models.Model):
    poll_name = models.CharField('Название', max_length=60)
    start_date = models.DateField('дата старта', default=date.today)
    finish_date = models.DateField('Дата окончания', default=date.today)
    description = models.TextField('Описание', max_length=1000)

    def __str__(self):
        return self.poll_name

class Choice(models.Model):
    question = models.ForeignKey(Polls, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    answer_text = models.CharField(max_length=100)
    ANSWER_CHOICES = (
        ("Y", "Yes"),
        ("N", "No"),

    )
    ANSWER_TYPE = (
        ("1", "Multiple"),
        ("2","Text"),
        ("3", "Single")


    )
    answer_choices = models.CharField(max_length=10, choices=ANSWER_CHOICES, default=1)
    answer_type = models.CharField(max_length=30, choices=ANSWER_TYPE, default=1)


    def __str__(self):
        return self.choice_text


class User(models.Model):
    user_name = models.CharField('Имя пользователя', max_length=10)
    user_answer = models.CharField(Choice,'Ответы польователя', max_length=200)

    def __str__(self):
        return self.user_name

