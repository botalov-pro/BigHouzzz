from django.db import models


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

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'
