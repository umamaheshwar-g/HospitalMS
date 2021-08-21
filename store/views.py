from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models.customer import Customer
from .models.doctor import Doctor
from .models.patient import Patients

# Create your views here.
def home(request):
    return render(request, 'home.html')

def main(request):
    return render(request, 'main.html')

def mainlog(request):
    return render(request, 'mainlog.html')

def psignup(request):
    if request.method == 'GET':
        return render(request, 'psignup.html')
    else:
        f = request.POST.get("firstname")
        l = request.POST.get("lastname")
        e = request.POST.get("email")
        p = request.POST.get("password")

        customer = Customer(first_name = f, last_name = l,email = e,password = p)
        error_message = None
        if (not f):
            error_message = "First Name Required !!"
        elif customer.isExists():
            error_message = "Email Allready Exists !!"

        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect("plogin")
        else:
            return render(request, 'psignup.html', {'error' : error_message})



def docsignup(request):
    if request.method == 'GET':
        return render(request, 'docsignup.html')
    else:
        f = request.POST.get("firstname")
        l = request.POST.get("lastname")
        s = request.POST.get("special")
        e = request.POST.get("email")
        p = request.POST.get("password")

        doctor = Doctor(name = f,last_name = l, special = s,email = e, password = p)
        error_message = None
        if (not f):
            error_message = "First Name Required !!"
        elif doctor.isExists():
            error_message = "Email Allready Exists !!"

        if not error_message:
            doctor.password = make_password(doctor.password)
            doctor.register()
            return redirect("doclogin")
        else:
            return render(request, 'docsignup.html', {'error' : error_message})



def plogin(request):
    if request.method == 'GET':
       return render(request, 'plogin.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                return redirect("home")
            else:
                error_message = "Email Or Password Invalid !!"
        else:
            error_message = "Email Or Password Invalid !!"
            print(email, password)
        return render(request, 'plogin.html', {'error' : error_message})

def logout(request):
    request.session.clear()
    return redirect('main.html')

def doclogin(request):
    if request.method == 'GET':
        return render(request, 'doclogin.html')
    else:
        postData = request.POST
        email = postData.get('email')
        password = postData.get('password')
        doctor = Doctor.get_doctor_by_email(email)
        error_message = None
        if doctor:
            flag = check_password(password, doctor.password)
            if flag:
                request.session['doctor'] = doctor.id
                return redirect("dochome")
            else:
                error_message = "Email Or Password Invalid !!"
        else:
            error_message = "Email OR Password Invalid !!"
            print(email, password)
        return render(request, 'doclogin.html', {'error' : error_message})

def dochome(request):
    return render(request, 'dochome.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def appointment(request):
    if request.method == 'GET':
        doctors = Doctor.get_all_doctors()
        return render(request, 'appointment.html', {'doctors' : doctors})
    else:
        f = request.POST.get("firstname")
        l = request.POST.get("lastname")
        a = request.POST.get("address")
        p = request.POST.get("phone")
        p = request.POST.get("product")

        doctor = Doctor.objects.filter(name=p).first()

        patient = Patients(first_name = f,last_name = l,address = a,phone = p,doctor = doctor)
        patient.register()
        return redirect("home")