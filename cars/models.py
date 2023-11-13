from django.db import models


class Vehicle(models.Model):
    Regnum = models.CharField('Регистрационный знак', max_length=10, db_index=True)
    IsRegnumAlien = models.BooleanField('Иностранный?', default=False)
    Model = models.CharField('Модель', max_length=200)
    Color = models.CharField('Цвет', max_length=200, default=None)
    Created = models.DateTimeField('Дата создания', auto_now_add=True)
    Updated = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Транспортное средство'
        verbose_name_plural = 'Транспортные средства'
        ordering = ('Regnum',)

    def __str__(self):
        return self.Regnum
