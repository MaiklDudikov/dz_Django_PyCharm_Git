from django.db import models


# Модель Покупатель (Customer)
class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя покупателя")
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Телефон")

    def __str__(self):
        return self.name


# Модель Продавец (Seller)
class Seller(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя продавца")
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Телефон")

    def __str__(self):
        return self.name


# Модель Товар (Product)
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название товара")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена товара")

    def __str__(self):
        return self.name


# Модель Продажа (Sale)
class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Покупатель")
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, verbose_name="Продавец")
    date = models.DateField(verbose_name="Дата продажи")
    quantity = models.PositiveIntegerField(verbose_name="Количество")

    def __str__(self):
        return f"{self.product.name} - {self.customer.name} - {self.quantity} шт."
