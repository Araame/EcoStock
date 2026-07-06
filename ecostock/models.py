from django.db import models

# Create your models here.
class Warehouse(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    title = models.CharField(max_length=25, verbose_name="Warehouse'")
    location = models.CharField(max_length=30, verbose_name="Warehouse's location")
    capacity = models.IntegerField(verbose_name="Warehouse's capacity")

class Product(models.Model):

    class Status(models.TextChoices):
        Avalaible = 'avalaible','Avalaible'
        Perime = 'perime','Perime'
        reserved = 'reserved', 'Reserved'


    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=30, verbose_name="Product's name")
    quantity = models.IntegerField(verbose_name="Quantity")
    description = models.CharField(max_length=50, verbose_name="Description")
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    status = models.CharField(choices = Status.choices, default = Status.Avalaible, verbose_name="Status")

    

   

