from django.db import models


class VehicleCategory(models.Model):
    """ Категория транспортного средства """
    name = models.CharField('Категория', max_length=100)
    icon = models.ImageField(
        'Путь до иконки',
        upload_to='img_category'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class VehicleBrand(models.Model):
    """ Марка транспортного средства """
    vehicle_brand = models.CharField('Марка ТС', max_length=100)

    def __str__(self):
        return self.vehicle_brand

    class Meta:
        verbose_name = 'Марка ТС'
        verbose_name_plural = 'Марка ТС'


class VehicleModel(models.Model):
    """ Транспортное средство """
    vehicle_model = models.CharField(max_length=255, verbose_name='Модель ТС')

    def __str__(self):
        return self.vehicle_model

    class Meta:
        verbose_name = 'Модель ТС'
        verbose_name_plural = 'Модель ТС'


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
