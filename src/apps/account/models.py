from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username=models.CharField('username', max_length=150,unique=True, blank=True,default='username')
    avatar=models.ImageField('Avatar', upload_to='user/avatar/', default='default/the-human-icon-and-logo-vector.jpg')
    email=models.EmailField('Email', unique=True)
    birthday=models.DateField('Birthday', null=True, blank=True)
    mobile=models.CharField('Mobile', max_length=100, null=True, blank=True)
    date_joined=models.DateTimeField('Joined data', auto_now_add=True)

    REQUIRED_FIELDS=['username']
    USERNAME_FIELD='email'

    class Meta:
        verbose_name='User'
        verbose_name_plural='Users'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    