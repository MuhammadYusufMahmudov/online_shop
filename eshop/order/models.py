from django.db import models
from account.models import Customer
from product.models import Product

"""
    Agar o'chib ketsa on_deletega(SET_NULL, null=True)
    Agar hammasi o'chib ketsa on_deletega( CASCADE)

    related_name ---> juda ham qulay metod
    yani customer.orders desak shunga taluqli hamma narsalarni ro'yxati chiqib keladi 
    
    
"""


class Order(models.Model):
    STATUSES = [
        ('PENDING', 'pending'),  # zakar bajarilishi kutilmoqda
        ('INPROGRESS', 'inprogress'),  # Jarayon
        ('COMPLATED', 'complated'),  # tugatildi
        ('CANCELED', 'canceled')  # Atkaz qilindi
    ]
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True)  # buyurtma vaqti
    required_date = models.DateTimeField(null=True)  # talab qilingan vaqt
    shipped_date = models.DateTimeField(null=True)  # yetkazilgan vaqt
    canceled_date = models.DateTimeField(null=True)  # atkaz qilingan vaqt
    status = models.CharField(max_length=10, choices=STATUSES, default='PENDING')  # Jarayon holat

    def __str__(self):
        return f'{self.customer.__str__()} -- order:{self.id}'

    def item_count(self):
        return self.details.count()

    def total_price(self):
        return sum(i.total_price() for i in self.details.all())


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='details')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='orders')
    quantity = models.IntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity

    def change_quantity(self, action, value=None):
        if action == 'plus':
            if self.quantity + 1 <= self.product.quantity:
                self.quantity += 1
        elif action == 'minus':
            if self.quantity - 1 > 1:
                self.quantity -= 1
        elif value:
            value = int(value)
            if value>self.product.quantity:
                value = self.product.quantity
            elif value<1:
                value = 1
            self.quantity = value
        self.save()




    def __str__(self):
        return f'order: {self.order.id} - {self.product}, quantity: {self.quantity}'
