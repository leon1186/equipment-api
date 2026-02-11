from django.db import models

# Create your models here.
class Equipment(models.Model):
    name=models.CharField(max_length=200)
    serial_number=models.CharField(max_length=200)
    status=models.CharField(max_length=50)


    def __str__(self):
        return self.name
    

class MaintenanceRecord(models.Model):

    equipment = models.ForeignKey(Equipment,on_delete=models.CASCADE)
    description= models.TextField()
    date_peformed= models.DateField()
    technician=models.CharField(max_length=200)


