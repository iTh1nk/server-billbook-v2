import uuid

from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from django.utils.translation import ugettext_lazy as _

from server_billbook_v2.settings import AUTH_USER_MODEL


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Email is required for User!')

        user = self.model(email=self.normalize_email(email),)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        if password is None:
            raise TypeError('Password is required for Superuser!')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        verbose_name='email address', max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = "login"


class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50, unique=False)
    last_name = models.CharField(max_length=50, unique=False)
    phone_number = models.CharField(
        max_length=10, null=False, blank=False)
    age = models.PositiveIntegerField(null=False, blank=False)
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'),)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    class Meta:
        db_table = "profile"


class Cycles(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False, unique=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.date

    # class Meta:
    #     ordering = ['date']


class Statements(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_statements')
    cycle = models.ForeignKey(
        Cycles, on_delete=models.CASCADE, related_name='cycle_statements')
    balance = models.CharField(max_length=255)
    notes = models.TextField()
    createdAt = models.DateField(auto_now_add=True)
    updateAt = models.DateField(auto_now=True)

    def __str__(self):
        return self.balance


class Activities(models.Model):
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='user_activities', null=False)
    date = models.DateField()
    amount = models.CharField(max_length=255)
    totalBalance = models.CharField(max_length=255)
    createdAt = models.DateField(auto_now_add=True)
    updateAt = models.DateField(auto_now=True)

    def __str__(self):
        return self.totalBalance
