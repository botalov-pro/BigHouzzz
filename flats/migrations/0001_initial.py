# Generated by Django 4.1.10 on 2023-12-21 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=3, verbose_name='Номер дома')),
                ('cad_number', models.CharField(blank=True, max_length=18, null=True, verbose_name='Кадастровый номер дома')),
                ('slug', models.SlugField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')),
            ],
            options={
                'ordering': ('number',),
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=3, verbose_name='Номер квартиры')),
                ('enter', models.PositiveSmallIntegerField(default=0, verbose_name='Подъезд')),
                ('level', models.SmallIntegerField(default=0, verbose_name='Этаж')),
                ('cad_number', models.CharField(blank=True, max_length=18, null=True, verbose_name='Кадастровый номер')),
                ('area', models.FloatField(blank=True, null=True, verbose_name='Площадь помещения')),
                ('ceiling_height', models.FloatField(blank=True, null=True, verbose_name='Высота потолков')),
                ('slug', models.SlugField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='house_rooms', to='flats.house', verbose_name='Дом')),
            ],
            options={
                'ordering': ('number',),
            },
        ),
    ]