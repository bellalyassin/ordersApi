from django.db import models

# Create your models here.
class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    clientId=models.IntegerField(max_length=120)
    restaurantId=models.IntegerField(max_length=120)
    productId = models.IntegerField(max_length=120)
    deliverymanId = models.IntegerField(max_length=120)
    status = models.TextField()
    dateOrder = models.DateTimeField()
    dateChangingStatus = models.DateTimeField()


