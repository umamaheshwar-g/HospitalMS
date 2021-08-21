from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    special = models.CharField(max_length=100)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=200)


    def register(self):
        return self.save()

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_doctors():
        return Doctor.objects.all()


    @staticmethod
    def get_doctor_by_email(email):
        try:
            return Doctor.objects.get(email = email)
        except:
            return False


    def isExists(self):
        if Doctor.objects.filter(email = self.email):
            return True

        return False