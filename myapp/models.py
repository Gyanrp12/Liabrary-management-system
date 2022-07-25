from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date, timedelta

choices = (('user', 'user'), ('librarian', 'librarian'),)


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=11)
    email = models.EmailField(max_length=255, unique=True)
    user_type = models.CharField(max_length=255, choices=choices)
    password = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return str(self.name)


def expiry():
    return date.today() + timedelta(days=7)


class IssuedBook(models.Model):
    student_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issued_date = models.DateField(auto_now=True)
    expiry_date = models.DateField(default=expiry)
