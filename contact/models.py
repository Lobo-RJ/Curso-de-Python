from django.db import models
from django.utils import timezone


class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=255)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/%d')

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
