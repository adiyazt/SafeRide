from django.db import models
import uuid

class Client(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, verbose_name='ID'
    )
    number = models.CharField(
        max_length=12, blank=False, verbose_name='Номер', unique=True
    )
    name = models.CharField(
        max_length=120, blank=False, verbose_name='Имя'
    )
    password = models.CharField(
        max_length=64, blank=False, verbose_name='Пароль'
    )
    bank = models.FloatField(
        default=0.0, blank=True, verbose_name='Счет'
    )
    rating = models.FloatField(
        default=5.0, blank=True, verbose_name='Рейтинг'
    )
    geoposition = models.CharField(
        default='49.8000567 73.0895435', blank=False, verbose_name='Локация', max_length=120
    )

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['-rating']


    def __str__(self):
        return self.name
    

    def is_valid(self) -> bool:
        return True
    

class Courier(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, verbose_name='ID'
    )
    number = models.CharField(
        max_length=12, blank=False, verbose_name='Номер', unique=True
    )
    name = models.CharField(
        max_length=120, blank=False, verbose_name='Имя'
    )
    password = models.CharField(
        max_length=64, blank=False, verbose_name='Пароль'
    )
    bank = models.FloatField(
        default=0.0, blank=True, verbose_name='Счет'
    )
    rating = models.FloatField(
        default=5.0, blank=True, verbose_name='Рейтинг'
    )
    geoposition = models.CharField(
        default='49.8000567 73.0895435', blank=False, verbose_name='Локация', max_length=120
    )

    class Meta:
        verbose_name = 'Курьер'
        verbose_name_plural = 'Курьеры'
        ordering = ['-rating']


    def __str__(self):
        return self.name
    

    def is_valid(self) -> bool:
        return True
    

class Taxist(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, verbose_name='ID'
    )
    number = models.CharField(
        max_length=12, blank=False, verbose_name='Номер', unique=True
    )
    name = models.CharField(
        max_length=120, blank=False, verbose_name='Имя'
    )
    password = models.CharField(
        max_length=64, blank=False, verbose_name='Пароль'
    )
    bank = models.FloatField(
        default=0.0, blank=True, verbose_name='Счет'
    )
    rating = models.FloatField(
        default=5.0, blank=True, verbose_name='Рейтинг'
    )
    geoposition = models.CharField(
        default='49.8000567 73.0895435', blank=False, verbose_name='Локация', max_length=120
    )
    is_free = models.BooleanField(
        default=True, verbose_name='Свободен?'
    )

    class Meta:
        verbose_name = 'Таксист'
        verbose_name_plural = 'Таксист'
        ordering = ['-rating']


    def __str__(self):
        return self.name
    

    def is_valid(self) -> bool:
        return True