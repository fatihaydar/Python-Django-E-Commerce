from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from product.models import Product


class Contact(models.Model):
    STATUS = (
        (1, 'New'),
        (2, 'Read'),
    )
    ad=models.CharField(max_length=255)
    mail=models.CharField(max_length=255)
    konu = models.CharField(max_length=255)
    mesaj= models.TextField(max_length=255)
    status = models.IntegerField(choices=STATUS, default=1)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.konu


class Comment(models.Model):
    STATUS=(
        (1,'true'),
        (2,'false'),
    )

    RATING= (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
    )

    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=60)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    message = models.TextField(max_length=255)
    status = models.IntegerField(choices=STATUS, default=2)
    rating = models.IntegerField(choices=RATING, default=0)
    create_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.subject