from django.db import models
from shop.models import Product
from orders.models import Order

class AccountProfile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    order = models.ForeignKey(Order,
                                related_name='account_orders+',
                                on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                            related_name = 'account_products',
                            on_delete=models.CASCADE)
