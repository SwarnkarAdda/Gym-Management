from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Member,Trainer,Admin
from django.core.mail import send_mail

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        
        admin_detail=Admin.objects.get(id=2)
        
        if username==admin_detail.email and password==admin_detail.password:
            return redirect('home')
        else:
            return redirect('error') # or render a custom error page
    return render(request, "Login.html",{'form':'Login'})

def Home(request):
    return render(request, 'home.html')

def NewMember(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        joiningDate = request.POST['joiningDate']
        expireingDate= request.POST['expireingDate']
        workoutTime = request.POST['workoutTime']
        plan = request.POST['plan']

        member=Member(name=name,age=age,gender=gender,email=email,phone=phone,address=address,joiningDate=joiningDate,expireingDate=expireingDate,workoutTime=workoutTime,plan=plan)
        member.save()

        subject = "Elite Gym Membership Confirmation"
        message = f"Hi {name},\n\nThank you for joining Elite Gym!\nYour membership has been successfully registered.\n\nPlan: {plan}\nWorkout Time: {workoutTime}\n\nStay strong!"
        recipient = [email]
        send_mail(subject, message, None, recipient)

        return redirect('successful')
    return render(request, 'NewMember.html')

def NewTrainer(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        experience = request.POST['experience']
        specialty = request.POST['specialty']
        joiningDate = request.POST['joiningDate']
        salary = request.POST['salary']
        shift = request.POST['shift']
    
        trainer=Trainer(name=name,age=age,gender=gender,email=email,phone=phone,address=address,experience=experience,specialty=specialty,joiningDate=joiningDate,salary=salary,shift=shift)
        trainer.save()

        subject = "Welcome to Elite Gym – Trainer Confirmation"
        message = f"Hi {name},\n\nWelcome to Elite Gym!\nYour trainer profile has been successfully registered.\n\nSpecialty: {specialty}\nShift: {shift}\nJoining Date: {joiningDate}\n\nGlad to have you on board!\n\n- Elite Gym Team"
        recipient = [email]

        send_mail(subject, message, None, recipient)

        return redirect('successful')
    return render(request, 'NewTrainer.html')

def Successful(request):
    return render(request, 'Successful.html')

def Error(request):
    return render(request, 'Error.html')

def MemberList(request):
    member = Member.objects.all()
    return render(request, 'MemberList.html', {'members': member})

def TrainerList(request):
    trainer = Trainer.objects.all()
    return render(request, 'TrainerList.html', {'trainers': trainer})

def SearchedMem(request):
        select = request.POST['select']
        search = request.POST['search']

        if select == "id":
            filter_kwargs = {select: int(search)}
        else:
            filter_kwargs = {select: search}

        try:
            members = Member.objects.filter(**filter_kwargs)
        except:
            members = []  # fallback if field is invalid

        return render(request, 'SearchMember.html', {'members': members})

def SearchedTra(request):
        select = request.POST['select']
        search = request.POST['search']

        if select == "id":
            filter_kwargs = {select: int(search)}
        else:
            filter_kwargs = {select: search}

        try:
            trainer = Trainer.objects.filter(**filter_kwargs)
        except:
            trainer = []  # fallback if field is invalid

        return render(request, 'SearchTrainer.html', {'trainers': trainer})

def delete_member(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return redirect('successful') 

def update_member(request, id):
    member = Member.objects.get(id=id)
    
    if request.method == "POST":
        member.name= request.POST['name']
        member.age= request.POST['age']
        member.email= request.POST['email']
        member.phone= request.POST['phone']
        member.address= request.POST['address']
        member.joiningDate= request.POST['joiningDate']
        member.expireingDate= request.POST['expireingDate']
        member.workoutTime= request.POST['workoutTime']
        member.plan= request.POST['plan']
        member.save()
        return redirect('successful')
    return render(request, 'UpdateMember.html', {'member': member})
 
def delete_trainer(request, id):
    trainer = Trainer.objects.get(id=id)
    trainer.delete()
    return redirect('successful') 

def update_trainer(request, id):
    trainer = Trainer.objects.get(id=id)
    
    if request.method == "POST":
        trainer.name= request.POST['name']
        trainer.age= request.POST['age']
        trainer.email= request.POST['email']
        trainer.phone= request.POST['phone']
        trainer.address= request.POST['address']
        trainer.specialty= request.POST['specialty']
        trainer.joiningDate= request.POST['joiningDate']
        trainer.salary= request.POST['salary']
        trainer.shift= request.POST['shift']
        trainer.save()
        return redirect('successful')
    return render(request, 'UpdateTrainer.html', {'trainer': trainer})

def About(request):
    return render(request, 'About.html')

def Contact(request):
    return render(request, 'Contact.html')