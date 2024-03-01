from django.db import models

# Create your models here.
class Employees(models.Model):
    name=models.CharField(max_length=100)
    checkIn=models.DateTimeField(auto_now_add=True)
    checkOut=models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.name
    

class diabetes(models.Model):
    glocose=models.FloatField(max_length=10)
    bmi=models.FloatField(max_length=10)
    prusser=models.FloatField(max_length=10)

    def __str__(self) :
        return self.glocose
    
class clothes(models.Model):
    name=models.CharField(max_length=100)
    price=models.FloatField(max_length=10)
    descreption=models.TextField()

    def __str__(self) :
        return self.name