from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
#    birth_date = models.DateField(blank=True, null=True)
    avatar = models.ImageField(
        'Аватар',
        upload_to='users_images',
        blank=True,
        null=True
    )
    agreement_accepted = models.BooleanField(
        'Пользовательское соглашение',
        default=False
    )
