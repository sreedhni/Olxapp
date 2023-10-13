from django.db import models

# Create your models here.
class OlxCreate(models.Model):
    vehiclename=models.CharField(max_length=100)
    company=models.CharField(max_length=300)
    number=models.CharField(max_length=15)
    price=models.PositiveIntegerField()
    phone=models.IntegerField()
    image=models.ImageField(upload_to="images",null=True)


    def __str__(self):
        return self.name


