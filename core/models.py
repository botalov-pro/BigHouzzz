from django.db import models
from users.models import User


class Colors(models.Model):
    """ Цвета """

    # DATABASE FIELDS
    name = models.CharField(
        'Цвет',
        max_length=100
    )
    description = models.TextField(
        'Описание',
        blank=True
    )
    is_active = models.BooleanField(
        verbose_name='Активна',
        default=True
    )

    # META CLASS
    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    # TO STRING METHOD
    def __str__(self):
        return self.name


class Review(models.Model):
    """ Отзыв """

    # CHOICES
    RATING_CHOICES = (
        ('5', '5'),
        ('4', '4'),
        ('3', '3'),
        ('2', '2'),
        ('1', '1'),
    )

    # DATABASE FIELDS
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    rating = models.CharField(
        'Оценка',
        max_length=1,
        choices=RATING_CHOICES,
        blank=True,
    )
    text = models.TextField(
        'Текст отзыва',
        max_length=250,
        blank=True,
    )
    is_active = models.BooleanField(
        'Активный',
        default=True
    )
    created = models.DateTimeField(
        'Дата создания',
        auto_now_add=True
    )

    # META CLASS
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('created',)

    # TO STRING METHOD
    # def __str__(self):
    #    return self.id
