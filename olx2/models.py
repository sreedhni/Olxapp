from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class OlxCreate(models.Model):
    vehiclename=models.CharField(max_length=100)
    company=models.CharField(max_length=300)
    number=models.CharField(max_length=15)
    price=models.PositiveIntegerField()
    phone=models.IntegerField()
    image=models.ImageField(upload_to="images",null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)



    def __str__(self):
        return self.vehiclename


