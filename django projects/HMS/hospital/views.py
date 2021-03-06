from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Doctor, Patient, Appointment
# Create your views here.
def home(request):
    return render(request, 'home.htm')
    
def index(request):
    return render(request, 'index.htm')

def about(request):
    return render(request, 'about.htm')

def contact(request):
    return render(request, 'contact.htm')

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    appointments = Appointment.objects.all()
    d = 0
    p = 0
    a = 0
    for i in doctors:
        d += 1
    for i in patients:
        p += 1
    for i in appointments:
        a += 1
    d1={'d':d, 'p':p, 'a':a}
    return render(request, 'index.htm', d1)

def Login(request):
    error = ""
    if request.method == "POST":
        username_a = request.POST['uname']
        password_a = request.POST['pwd']
        user = authenticate(username = username_a,password = password_a)
        try :
            if user.is_staff:
                login(request,user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error':error}
    return render(request,'login.htm', d )

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')

#doctor section
def View_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    d = {'doc' : doc}
    return render(request,'view_doctor.htm', d)

def Delete_doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id = pid)
    doctor.delete()
    return redirect('view_doctor')

def Add_doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == "POST":
        name_d = request.POST['name']
        mobile_d = request.POST['mobile']
        sp_d = request.POST['special']
        try :
            Doctor.objects.create(name=name_d,mobile=mobile_d,special=sp_d)
            error = 'no'
        except:
            error = 'yes'
    d = {'error' : error}
    return render(request,'add_doctor.htm', d )

#patient---------
def View_patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pat = Patient.objects.all()
    p = {'pat' : pat}
    return render(request,'view_patient.htm', p)

def Delete_patient(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id = pid)
    patient.delete()
    return redirect('view_patient')

def Add_patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == "POST":
        name_p = request.POST['name']
        gender_p = request.POST['gender']
        mobile_p = request.POST['mobile']
        address_p = request.POST['address']
        try :
            Patient.objects.create(name=name_p,gender=gender_p,mobile=mobile_p,address=address_p)
            error = 'no'
        except:
            error = 'yes'
    d = {'error' : error}
    return render(request,'add_patient.htm', d )

#appointment
def View_appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    apt = Appointment.objects.all()
    p = {'apt' : apt}
    return render(request,'view_appointment.htm', p)

def Delete_appointment(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    appointment = Appointment.objects.get(id = pid)
    appointment.delete()
    return redirect('view_appointment')

def Add_appointment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    pat = Patient.objects.all()
    if request.method == "POST":
        
        d_name = request.POST['doctor']
        p_name = request.POST['patient']
        date_a = request.POST['date']
        time_a = request.POST['time']
        doctor = Doctor.objects.filter(name=d_name).first()
        patient = Patient.objects.filter(name=p_name).first()
        try :
            Appointment.objects.create(doctor=doctor,patient=patient,date=date_a,time=time_a)
            error = 'no'
        except:
            error = 'yes'
    d = {'doctor' : doc,'patient' : pat,'error' : error}
    return render(request,'add_appointment.htm', d )