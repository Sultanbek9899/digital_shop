from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField("Название", max_length=200)
    description = models.TextField("Описание", blank=True, null=True)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    is_active = models.BooleanField("Активный", default=True)
    created = models.DateTimeField("Дата создание", auto_now_add=True)
    updated = models.DateTimeField("Дата обновления", auto_now=True)
    quantity = models.PositiveIntegerField("Количество", default=0)

    class Meta:
        ordering = ["-created"]
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name


