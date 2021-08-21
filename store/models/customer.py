from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=200)

    def register(self):
        return self.save()

    def __str__(self):
        return self.first_name


    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email = email)
        except:
            return False



    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return False