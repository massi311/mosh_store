from django.db import models

# Create your models here.
class Collection(models.Model):
    title=models.CharField(max_length=255)


class Product(models.Model):
    title = models.CharField(max_length=255)
    description=models.CharField()
    slug=models.SlugField()
    price=models.DecimalField(max_digits=6,decimal_places=2)
    inventory=models.IntegerField()
    last_update=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    collection=models.ForeignKey(Collection,on_delete=models.PROTECT,null=True)
    def __str__(self):
        return self.title




class Customer(models.Model):
    MEMBERSHIP_BRONZE="B"
    MEMBERSHIP_SILVER="S"
    MEMBERSHIP_GOLD="G"
    MEMBERSHIP_CHOICES=[
        (MEMBERSHIP_BRONZE,'Bronze'),
        (MEMBERSHIP_SILVER,'Silver'),
        (MEMBERSHIP_GOLD,'Gold'),
    ]
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200,unique=True)
    phone=models.CharField(max_length=22)
    birth_date=models.DateField(null=True)
    membership=models.CharField(max_length=1,choices=MEMBERSHIP_CHOICES,default=MEMBERSHIP_BRONZE)
    def __str__(self):
        return self.first_name



class Order(models.Model):
    PAYMENT_PENDING="P"
    PAYMENT_COMPLETE="C"
    PAYMENT_FAILED="F"
    PAYMENT_CHOICES=[
        (PAYMENT_PENDING,"PENDING"),
        (PAYMENT_COMPLETE,"COMPLETE"),
        (PAYMENT_FAILED,"FAILED"),
    ]
    placed_at=models.DateTimeField(auto_now_add=True)
    payment_status=models.CharField(max_length=1,choices=PAYMENT_CHOICES)
    customer=models.ForeignKey(Customer,on_delete=models.PROTECT)


class address(models.Model):
    street=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)

class Cart(models.Model):
    ceated_at=models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveSmallIntegerField()


class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.PROTECT)
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity=models.PositiveSmallIntegerField()
    unit_price=models.DecimalField(max_digits=6,decimal_places=2)