# picks/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Remove the username field and use email instead.
    username = None
    email = models.EmailField('email address', unique=True)
    phone_number = models.CharField(max_length=15)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']

    def __str__(self):
        return self.email

class Game(models.Model):
    team = models.CharField(max_length=50)
    # Renamed from "date" to "week" to better reflect the schedule.
    week = models.CharField(max_length=20)  # e.g., "Week 1", "Week 2", etc.
    opponent = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.team} vs {self.opponent} in {self.week}"

class Pick(models.Model):
    PICK_CHOICES = (
        ('W', 'Win'),
        ('L', 'Loss'),
    )
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    pick = models.CharField(max_length=1, choices=PICK_CHOICES)

    class Meta:
        unique_together = ('user', 'game')

    def __str__(self):
        return f"{self.user.email}: {self.game} - {self.pick}"
