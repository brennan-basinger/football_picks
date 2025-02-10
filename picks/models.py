# picks/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Custom user manager where email is the unique identifiers for authentication.
    """

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        # Set the required fields for a superuser.
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self.create_user(email, password, **extra_fields)



class User(AbstractUser):
    # Remove the default username field.
    username = None
    email = models.EmailField('email address', unique=True)
    phone_number = models.CharField(max_length=15)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']

    # Set the custom user manager.
    objects = CustomUserManager()

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
