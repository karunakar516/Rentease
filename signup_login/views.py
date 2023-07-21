from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import signup_form,formss,addhouse,password_reset
from .models import house
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from random import randint
from rentease import settings
from django.core.mail import send_mail
from .models import current_signup,house
def index(request):
    return render(request,'user-new.html')
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('signup_login:home'))
@login_required
def deleteacc(request):
    if request.method=='POST':
        user=request.user
        username=request.POST.get('username')
        if username==user.username:
            x=User.objects.get(username=username)
            x.delete()
            return HttpResponseRedirect(reverse('signup_login:home'))
    else:
        return render(request,'deleteacc.html')
@login_required
def addhouse1(request):
    if request.method=="POST":
        ahform=addhouse(request.POST,request.FILES)
        if ahform.is_valid:
            ahform.save()
            return HttpResponseRedirect(reverse('signup_login:home'))
    else:
        ahform=addhouse(initial={'userid':request.user.username})
        return render(request,'addHouse.html',{'form':ahform})
@login_required
def passreset(request):
    if request.method=="POST":
        user=request.user
        if user.is_active:
            password=request.POST.get('password')
            user.set_password(password)
            user.save()
            login(request,user)
            return HttpResponseRedirect(reverse('signup_login:home'))
        else:
            return HttpResponse('nope')
    else:
        form=password_reset()
        return render(request,'password-reset.html',{'form':form})
@login_required
def myhouses(request):
    userid=request.user.username
    x=house.objects.all()
    y=[]
    for i in x:
        if i.userid==userid:
            y.append(i)
    return render(request,'myhouse.html',{'houses':y})
@login_required
def house_deletion(request):
    if(request.method=='POST'):
        userid=request.user.username
        x=house.objects.get(userid=userid,houseid=request.POST.get('houseid'))
        x.delete()
        return HttpResponseRedirect(reverse('signup_login:home'))
    else:
        return render(request,'deletehouse.html')
def otpverify(request):
    if request.method=='POST':
        xx=request.POST.get('otp')
        yy=request.POST.get('username')
        xnxx=current_signup.objects.all()
        for i in xnxx:
            if int(i.x)==int(xx) and yy==i.username:
                form=signup_form({'username':i.username,'password':i.password,'email':i.email,'reppass':i.reppass})
                formsss=formss(data=request.POST)
                if form.is_valid() and formsss.is_valid():
                    user=form.save()
                    user.set_password(user.password)
                    user.save()
                    profile=formsss.save(commit=False)
                    profile.user=user
                    profile.save()
                    i.delete()
                    return HttpResponseRedirect(reverse('signup_login:home'))
                else:
                    return HttpResponse('invalid signup')
        else:
            return HttpResponse("wrong otp")
def register(request):
    global registered
    registered=False
    if request.method=='POST':
        otp=randint(1000,9999)
        x=otp
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        reppass=request.POST.get('reppass')
        xy=User.objects.all()
        for i in xy:
            if i.email==email or i.username==username:
                return HttpResponse("username already exists")
        xa=current_signup(username=username,password=password,reppass=reppass,email=email,x=x)
        xa.save(True)
        subject="Rentease!!"
        message="Hi,"+"\n" +request.POST.get('username')+" tried to signup for an account in RentEase with "+request.POST.get('email')+"If it was you,enter the confirmation code in the app\n"+"\n"+str(x)
        from_email=settings.EMAIL_HOST_USER
        to_mail=[request.POST.get('email')]
        send_mail(subject,message,from_email,to_mail)
        return render(request,'otp.html',{'username':username})
    else:
        form=signup_form()
        formsss=formss()
    return render(request,'login-new.html',{
        'form':form,
        'formsss':formsss,
        'registered':registered,
        'signup':True,
        
    })
def user_login(request):
    if request.method=='POST':
        un=request.POST.get('username_login')
        pwd=request.POST.get('password_login')
        x=User.objects.all()
        c=0
        for i in x:
            if i.username==un:
                c+=1
        if c==0:
            return HttpResponse("no user with entered username")
        user=authenticate(username=un,password=pwd)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('signup_login:home'))
            else:
                return HttpResponse('account not active')
        else:
            return HttpResponse('Password Not Correct')  
    else:
        return render(request,'login-new.html',{'login':True})
def search(request):
    ob=house.objects.all()
    return render(request,'search.html',{'houses':ob})
