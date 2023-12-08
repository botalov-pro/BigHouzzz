from django.contrib import admin
from django.utils.safestring import mark_safe
from BigHouzzz.settings import EMPTY_VALUE_DISPLAY
from users.models import User


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    """ Пользователи - Администрирование """
    fieldsets = [
        (
            None,
            {
                'fields': [
                    ('avatar_image', 'username'),
                    ('last_name', 'first_name', 'patronymic_name'),
                    ('email', 'phone_number'),
                    'birth_date',
                    'is_active',
                ],
            },
        ),
        (
            'Дополнительно',
            {
                "classes": ['collapse'],
                "fields": [
                    'agreement_accepted',
                    'verify',
                    'avatar',
                    ('last_login', 'date_joined'),
                ],
            },
        ),
    ]
    list_display = [
        'full_name',
        'avatar_image',
        'agreement_accepted',
        'last_login',
        'is_active',
    ]
    list_filter = [
        'is_staff',
        'is_active',
        'verify',
        'agreement_accepted',
        'last_login',
        'date_joined'
    ]
    search_fields = [
        'email',
        'username',
        'first_name',
        'last_name',
        'patronymic_name',
    ]
    readonly_fields = [
        'agreement_accepted',
        'avatar_image',
        'last_login',
        'date_joined',
    ]
    empty_value_display = EMPTY_VALUE_DISPLAY

    # Возвращаем изображение для аватарки
    def avatar_image(self, obj):
        if obj.avatar:
            return mark_safe(
                f'<img src="{obj.avatar.url}" alt="" height="50px">')
        else:
            return mark_safe(f'<img src="" alt="">')

    # Переназываем поле для изображения аватарки
    avatar_image.short_description = 'Аватар'

    # Возвращаем полное имя пользователя + имя пользователя
    @admin.display(description='Фамилия, имя, отчество (имя пользователя)')
    def full_name(self, obj):
        return f'{obj.last_name} {obj.first_name} {obj.patronymic_name} ({obj.username})'
