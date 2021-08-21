from django.contrib import admin
from .models.customer import Customer
from .models.doctor import Doctor
from .models.patient import Patients

# Register your models here.
class PatientInline(admin.StackedInline):
    list_display = ['first_name','last_name','address','phone','doctor']
    model = Patients
    extra = 0

class AdminDoctor(admin.ModelAdmin):
    inlines = [PatientInline]


class Adminappointment(admin.ModelAdmin):
    list_display = ['first_name','last_name','address','phone','doctor']

   



admin.site.register(Customer)
admin.site.register(Doctor,AdminDoctor)
admin.site.register(Patients,Adminappointment)

