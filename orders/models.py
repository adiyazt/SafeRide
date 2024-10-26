from django.db import models
import uuid
from django.utils.timezone import now

class TaxiOrder(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, verbose_name='ID'
    )
    client = models.CharField(
        max_length=120, blank=False, verbose_name='Клиент'
    )
    taxist = models.CharField(
        max_length=120, blank=False, verbose_name='Таксист'
    )
    number = models.CharField(
        max_length=12, blank=False, verbose_name='Номер'
    )
    distance = models.FloatField(
        blank=False, verbose_name='Расстояние'
    )
    price = models.FloatField(
        blank=False, verbose_name='Цена'
    )
    rating = models.FloatField(
        default=5.0, blank=True, verbose_name='Рейтинг'
    )
    start = models.DateTimeField(
        default=now, editable=False, blank=True, verbose_name='Начало'
    )
    end = models.DateTimeField(
        default=now, editable=False, blank=True, verbose_name='Конец'
    )
    is_active = models.BooleanField(
        default=False
    )

    class Meta:
        verbose_name = 'Заказ такси'
        verbose_name_plural = 'Заказы такси'
        ordering = ['-price']
    

    def is_valid(self) -> bool:
        return True
    

class DeliveryOrder(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, verbose_name='ID'
    )
    client = models.CharField(
        max_length=120, blank=False, verbose_name='Клиент'
    )
    recipient = models.CharField(
        max_length=120, blank=False, verbose_name='Получатель'
    )
    courier = models.CharField(
        max_length=120, blank=False, verbose_name='Курьер'
    )
    number = models.CharField(
        max_length=12, blank=False, verbose_name='Номер', unique=True
    )
    distance = models.FloatField(
        blank=False, verbose_name='Расстояние'
    )
    price = models.FloatField(
        blank=False, verbose_name='Цена'
    )
    rating = models.FloatField(
        default=5.0, blank=True, verbose_name='Рейтинг'
    )

    class Meta:
        verbose_name = 'Заказ доставки'
        verbose_name_plural = 'Заказы доставки'
        ordering = ['-price']
    

    def is_valid(self) -> bool:
        return True