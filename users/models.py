from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """ Пользователи """
    patronymic_name = models.CharField(
        'Отчество',
        max_length=50,
        blank=True
    )
    birth_date = models.DateField(
        'Дата рождения',
        blank=True,
        null=True
    )
    phone_number = models.CharField(
        'Номер телефона',
        max_length=12,
        blank=True
    )
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
    verify = models.BooleanField(
        'Верификация пользователя',
        default=False
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
