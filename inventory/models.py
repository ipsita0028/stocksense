from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['name']

    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    reorder_level = models.PositiveIntegerField(default=10)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    @property
    def is_low(self):
        return self.stock <= self.reorder_level
class StockEntry(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    added_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new:
            self.product.stock += self.quantity
            self.product.save()

    def __str__(self):
        return f"{self.product} +{self.quantity}"

class Customer(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15, blank=True)
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
class Bill(models.Model):
    CASH, CREDIT = 'cash', 'credit'
    PAYMENT_CHOICES = [(CASH, 'Cash'), (CREDIT, 'Credit')]

    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True, blank=True)
    payment_type = models.CharField(max_length=10, choices=PAYMENT_CHOICES, default=CASH)
    created_on = models.DateTimeField(auto_now_add=True)

    def total(self):
        return sum(item.subtotal() for item in self.billitem_set.all())

    def __str__(self):
        return f"Bill #{self.pk}"


class BillItem(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.quantity * self.price

    def __str__(self):
        return f"{self.product} x {self.quantity}"