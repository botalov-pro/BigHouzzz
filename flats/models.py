from django.db import models


class House(models.Model):
    """ Дом """
    number = models.CharField(
        verbose_name='Номер дома',
        max_length=3
    )    # Номер дома
    cad_number = models.CharField(
        verbose_name='Кадастровый номер дома',
        max_length=18,
        null=True,
        blank=True,
    )  # Кадастровый номер дома
    slug = models.SlugField(max_length=250)    # slug
    created = models.DateTimeField(
        verbose_name='Добавлено',
        auto_now_add=True
    )    # Дата создания


    class Meta:
        ordering = ('number',)    # Сортировка по номеру дома

    def __str__(self):
        return self.number    # Возвращать номер дома


class Room(models.Model):
    """ Помещение """
    number = models.CharField(
        verbose_name='Номер квартиры',
        max_length=3
    )    # Номер квартиры
    house = models.ForeignKey(
        House,
        verbose_name='Дом',
        on_delete=models.CASCADE,
        related_name='house_rooms'
    )    # Дом
    enter = models.PositiveSmallIntegerField(
        verbose_name='Подъезд',
        default=0,
    )    # Подъезд
    level = models.SmallIntegerField(
        verbose_name='Этаж',
        default=0,
    )    # Этаж
    cad_number = models.CharField(
        verbose_name='Кадастровый номер',
        max_length=18,
        null=True,
        blank=True,
    )    # Кадастровый номер квартиры
    area = models.FloatField(
        verbose_name='Площадь помещения',
        null=True,
        blank=True,
    )    # Площадь помещения
    ceiling_height = models.FloatField(
        verbose_name='Высота потолков',
        null=True,
        blank=True,
    )  # Высота потолков
    slug = models.SlugField(max_length=250)    # slug
    created = models.DateTimeField(
        verbose_name='Добавлено',
        auto_now_add=True
    )    # Дата создания

    class Meta:
        ordering = ('number',)    # Сортировка по номеру квартиры

    def __str__(self):
        return f'{self.house}, {self.number}'    # Возвращать дом и квартиру
