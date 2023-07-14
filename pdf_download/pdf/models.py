from django.db import models
from datetime import datetime

# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Product(models.Model):
    image=models.ImageField(upload_to='product_image',null=False,blank=False)
    name=models.CharField(max_length=50,null=False)
    price=models.IntegerField(null=False)
    description=models.TextField(max_length=200,null=False)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=False)
    create_at=models.DateTimeField(default=datetime.now)
    update_on=models.DateTimeField( auto_now=True)

    def __str__(self):
        return self.name


