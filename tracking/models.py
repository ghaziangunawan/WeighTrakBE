from django.db import models
from datetime import datetime

# Create your models here
class Me(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    body_fat = models.IntegerField(default=0)

class MuscleGroup(models.Model):
    name = models.CharField(max_length=20,primary_key=True)
    times_worked_this_week = models.IntegerField(default=0)

    def __str__ (self):
        return self.name

class Session(models.Model):
    date = models.DateTimeField()
    duration = models.DurationField() 
    notes = models.TextField(blank=True)  

class WorkOut(models.Model):
    workout_type = (
        ('S','Strength'),
        ('C','Cardio')
    )
    name = models.CharField(max_length=20,primary_key=True)
    type = models.CharField(max_length=1, choices=workout_type)
    description = models.TextField()

    def __str__(self):
        return self.name

class WorkOutSession(models.Model):
    workout = models.ForeignKey(WorkOut ,on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    weight = models.IntegerField()
    duration = models.DurationField()

class WorkOutMuscleGroup(models.Model):
    workout= models.ForeignKey(WorkOut, on_delete=models.CASCADE)
    muscle_group = models.ForeignKey(MuscleGroup, on_delete=models.CASCADE)