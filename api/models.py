from django.db import models


class Cycles(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


class Statements(models.Model):
    username = models.CharField(max_length=255)
    cycle = models.CharField(max_length=255)
    balance = models.CharField(max_length=255)
    notes = models.TextField()
    createdAt = models.DateField(auto_now_add=True)
    updateAt = models.DateField(auto_now=True)


class Activities(models.Model):
    username = models.CharField(max_length=255)
    date = models.DateField()
    amount = models.CharField(max_length=255)
    totalBalance = models.CharField(max_length=255)
    createdAt = models.DateField(auto_now_add=True)
    updateAt = models.DateField(auto_now=True)