from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from bicycles.constants import (MAX_DESCRIPTION_LENGTH, MAX_HOUR_PRICE,
                                MAX_NAME_LENGTH, MIN_HOUR_PRICE)

User = get_user_model()


class PriceType(models.Model):
    """Стоимость."""

    name = models.CharField('Название', max_length=MAX_NAME_LENGTH)
    price = models.PositiveSmallIntegerField(
        'Стоимость аренды',
        validators=[MinValueValidator(
            MIN_HOUR_PRICE,
            message='Укажите стоимость аренды'),
            MaxValueValidator(MAX_HOUR_PRICE,
                              message='Слишком дорого, проверьте цену')])

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'

    def __str__(self):
        return self.name


class RentedBicycleStatus(models.TextChoices):
    """Статусы для арендованных велосипедов."""

    RENTED = 'rented', _('Арендован')
    RETURNED = 'returned', _('Возвращен')
    DAMAGED = 'damaged', _('Велосипед поврежден или не возвращен вовремя')


class BicycleStatus(models.TextChoices):
    """Статусы для велосипедов."""
    AVAILABLE = 'availible', _('Доступен')
    RENTED = 'rented', _('Арендован')
    NOTAVAILABLE = 'notavailible', _('Недоступен по какой-то причине') 


class Bicycle(models.Model):
    """Велосипед."""

    name = models.CharField('Название велосипеда',
                            max_length=MAX_NAME_LENGTH)
    description = models.TextField(
        "Описание велосипеда",
        max_length=MAX_DESCRIPTION_LENGTH,
        null=True,
    )
    status = models.CharField('Статус', max_length=MAX_NAME_LENGTH,
                              choices=BicycleStatus.choices,
                              default=BicycleStatus.AVAILABLE)

    rental_cost = models.ForeignKey(
        PriceType,
        on_delete=models.CASCADE,
        related_name='bicycle',
        verbose_name='стоимость аренды',
    )

    class Meta:
        verbose_name = "Велосипед"
        verbose_name_plural = "Велосипеды"
        ordering = ["id"]

    def __str__(self):
        return self.name


class RentedBicycle(models.Model):
    """Арендованные велосипеды."""
    client = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='client',
        verbose_name='клиент',)
    bicycle = models.ForeignKey(
        Bicycle,
        on_delete=models.CASCADE,
        related_name='rented_bicycle',
        verbose_name='арендованный велосипед',)
    status = models.CharField('Статус', max_length=MAX_NAME_LENGTH,
                              choices=RentedBicycleStatus.choices,
                              default=RentedBicycleStatus.RENTED)
    rented_at = models.DateTimeField(
        verbose_name='Когда арендован',
        auto_now_add=True
    )
    returned_at = models.DateTimeField(
        verbose_name='Когда возвращен',
        null=True, blank=True,
    )

    class Meta:
        verbose_name = 'Арендованный велосипед'
        verbose_name_plural = 'Арендованные велосипеды'

    def __str__(self):
        return f'{self.client} арендовал {self.bicycle}'
