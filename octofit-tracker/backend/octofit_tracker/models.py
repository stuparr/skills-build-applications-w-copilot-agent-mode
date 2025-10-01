from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.CharField(max_length=100)
    activity = models.CharField(max_length=100)
    duration = models.IntegerField()  # in minutes
    date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Activities'
    
    def __str__(self):
        return f"{self.user} - {self.activity}"

class Leaderboard(models.Model):
    user = models.CharField(max_length=100)
    team = models.CharField(max_length=100, blank=True)
    total_minutes = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.user} - {self.total_minutes} mins"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()  # in minutes
    difficulty = models.CharField(max_length=20, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced')
    ])
    suggested_for = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.name
