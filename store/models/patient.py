from django.db import models
from .doctor import Doctor

class Patients(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,default=None, null=False, blank=False)


    def register(self):
        return self.save()