from django.db import models


class Promotions(models.Model):
    discount = models.FloatField()


class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    inventory = models.IntegerField()
    unit_price = models.DecimalField(max_digits=6,decimal_places=2)
    last_updated = models.DateField(auto_now=True)
    collection_id = models.ForeignKey(Collection,on_delete=models.PROTECT) 
    promotion_ids = models.ManyToManyField(Promotions)

class Customer(models.Model):
    MEMBER_BRONZE ='B'
    MEMBER_SILVER ='S'
    MEMBER_GOLD ='G'

    MEMBER_CHOICES = [
        (MEMBER_BRONZE, 'Bronze'),
        (MEMBER_SILVER, 'Silver'),
        (MEMBER_GOLD, 'Gold'),
    ]

    given_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1,choices=MEMBER_CHOICES, default=MEMBER_BRONZE)

    class Meta:
        indexes = [
            models.Index(fields=['given_name','last_name'])
        ]

class Order(models.Model):
    PAYMENT_STATUS_PENDING ='P'
    PAYMENT_STATUS_COMPLETE ='C'
    PAYMENT_STATUS_FAILED ='F'

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING,'P'),
        (PAYMENT_STATUS_COMPLETE,'C'),
        (PAYMENT_STATUS_FAILED,'F'),
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status= models.CharField(max_length=1,choices=PAYMENT_STATUS_CHOICES,default=PAYMENT_STATUS_PENDING)
    customer_id = models.ForeignKey(Customer,on_delete=models.PROTECT)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveSmallIntegerField()

class Address(models.Model):
    zip_field = models.CharField(max_length=255, null=True)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)


class Cart(models.Model):
    pass

class Item(models.Model):
    cart_id = models.ForeignKey(Cart,on_delete=models.CASCADE)
    oder_id = models.ForeignKey(Order, on_delete=models.PROTECT)