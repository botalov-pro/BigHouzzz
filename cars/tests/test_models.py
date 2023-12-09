from django.test import TestCase
from cars.models import VehicleCategory


class VehicleCategoryTests(TestCase):
    """ Тесты для модели VehicleCategory """

    @classmethod
    def setUpTestData(self):
        """ Заносит данные в БД перед запуском тестов класса """
        self.category = VehicleCategory.objects.create(
            name='Тестовый цвет'
        )
        self.name_field = self.category._meta.get_field('name')

    def test_verbose_name(self):
        """ Тест параметра verbose_name """
        real_verbose_name = getattr(self.name_field, 'verbose_name')
        expected_verbose_name = 'Категория'
        self.assertEqual(real_verbose_name, expected_verbose_name)

    def test_max_length(self):
        """ Тест параметра max_length """
        real_max_length = getattr(self.name_field, 'max_length')
        self.assertEqual(real_max_length, 100)

    def test_unique(self):
        pass

    def test_str_method(self):
        pass

    def test_model_verbose_name(self):
        """ Тест поля verbose_name модели VehicleCategory """
        self.assertEqual(VehicleCategory._meta.verbose_name, 'Категория ТС')

    def test_model_verbose_name_plural(self):
        """ Тест поля verbose_name_plural модели VehicleCategory """
        self.assertEqual(VehicleCategory._meta.verbose_name_plural, 'Категории ТС')