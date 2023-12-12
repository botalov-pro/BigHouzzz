from django.db import models
from core.models import Colors
from users.models import User

class VehicleCategory(models.Model):
    """ Категория транспортного средства """
    name = models.CharField('Категория', max_length=100)
    icon = models.ImageField(
        'Путь до иконки',
        upload_to='img_category',
        blank=True,
        null=True
    )
    is_active = models.BooleanField(
        'Активный',
        default=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория ТС'
        verbose_name_plural = 'Категории ТС'


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
    """ Транспортное средство """
    regnum = models.CharField(
        'Регистрационный знак',
        max_length=10,
        db_index=True
    )
    is_alien = models.BooleanField(
        'Иностранный?',
        default=False
    )
    category = models.ForeignKey(
        VehicleCategory,
        verbose_name='Тип ТС',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    model = models.CharField('Модель', max_length=200)
    color = models.ForeignKey(
        Colors,
        verbose_name='Цвет кузова',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    driver = models.ForeignKey(
        User,
        verbose_name='Водитель',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    created = models.DateTimeField(
        'Дата создания',
        auto_now_add=True
    )
    updated = models.DateTimeField(
        'Дата обновления',
        auto_now=True
    )
    is_active = models.BooleanField(
        'Активный',
        default=True
    )
    main_image = models.ImageField(
        'Основное изображение',
        upload_to='vehicles_images',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Транспортное средство'
        verbose_name_plural = 'Транспортные средства'
        ordering = ('regnum',)

    def __str__(self):
        return self.regnum
