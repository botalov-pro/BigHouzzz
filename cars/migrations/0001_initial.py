# Generated by Django 4.2.6 on 2023-11-07 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Regnum', models.CharField(db_index=True, max_length=10, verbose_name='Регистрационный знак')),
                ('IsRegnumAlien', models.BooleanField(default=False, verbose_name='Иностранный?')),
                ('Model', models.CharField(max_length=200, verbose_name='Регистрационный знак')),
                ('Color', models.CharField(default=None, max_length=200, verbose_name='Цвет')),
                ('Created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('Updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
            ],
            options={
                'verbose_name': 'Транспортное средство',
                'verbose_name_plural': 'Транспортные средства',
                'ordering': ('Regnum',),
            },
        ),
    ]