from django.db import models
from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):
    GENDER_CHOICE = (
        ('MALE', 'male'),
        ('FEMALE', 'female'),
    )
    """ Biz yana bitta obyekt yaratyapmiz shuning uchun makemigaratons qilishimiz kerek"""
    phone_number = models.CharField(
        max_length=155,
        unique=True
    )
    username = models.CharField(
        max_length=155,
        unique=True,
        null=True
    )
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, choices=GENDER_CHOICE)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    is_verified = models.BooleanField(default=False)  # bu teshirish
    image = models.ImageField(null=True, blank=True)

    USERNAME_FIELD = 'phone_number'  # misol uchun shu yerda phone_number bo'lishi mumkin endi va shu orqali registatsiyadan o'tardi
    REQUIRED_FIELDS = ['username', 'email']  # lekin biz username va email orqali ro'yxatdan o'tadi

    def __str__(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        else:
            return self.phone_number
