from django.db import models


class Colors(models.Model):
    """ Цвета """
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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'
