from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from userapp.models import *
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


# Create your views here.
def home(request):
    return render(request,"index.html",{})



def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        data = {
            'Name':name,
            'E-mail':email,
            'Subject':subject,
            'Message':message,
        }

        message = '''
        New message :{}

        From:{}
        '''.format(data['Message'],data['E-mail'])
        send_mail(data['Subject'],message,'',['kottarathilaswathi@gmail.com'])
        return HttpResponse("Thank you for the massage. We will see you soon")
    return render(request,"index.html",{})



def creg(request):
    msg=""
    if request.method=='POST':
        fname=request.POST.get('firstname')
        email=request.POST.get('email')
        password=request.POST.get('psw')
        repassword=request.POST.get('psw-repeat')
        address=request.POST.get('address')
        phone_no=request.POST.get('phone')
        qualification=request.POST.get('qual')
        experience=request.POST.get('exp')
        cv=request.POST.get('cv')
        if password==repassword:
            if tbl_candregistration.objects.filter(fname=fname):
                msg="Username already exist"
                return render(request,"registercandidate.html",{'msg':msg})
            else:
                if tbl_candregistration.objects.filter(password=password):
                    msg="Password already exist"
                    return render(request,"registercandidate.html",{'msg':msg})
                else:
                    data=tbl_candregistration.objects.create(fname=fname,email=email,password=password,address=address,phone_no=phone_no,qualification=qualification,experience=experience,cv=cv,status=1)
                    data=tbl_candlogin.objects.create(username=fname,password=password,status=1)
                    msg="Registration Successfully Done..."
                    return render(request,"registercandidate.html",{'msg':msg})
        else:
            msg="Password not match...!!!"
    return render(request,"registercandidate.html",{'msg':msg})










def clog(request):
    msg=""
    if request.method=='POST':
        username=request.POST.get('cname')
        password=request.POST.get('cpass')
        if tbl_candlogin.objects.filter(username=username,password=password):
            data=tbl_candregistration.objects.get(fname=username,password=password)
            request.session['userid']=data.id
            if data.status=='admin':
                return render(request,"registercandidate.html",{'msg':msg})
            elif data.status=='1':
                return render(request,"search.html",{'msg':msg})

        else:
            msg="Incorrect Username or password"
            # return HttpResponse("incorrect username or password")
           

    return render(request,"signincandidate.html",{'msg':msg})




@login_required
def csearch(request):
    return render(request,"search.html",{})






def jobsearch(request):
    
    if request.method=="POST":
        
        title=request.POST.get('title')
        location=request.POST.get('location')
        # if tbl_jobsearch.objects.filter(jtitle=title,jlocation=location):
        data=tbl_compdetails.objects.filter(jobtitle=title,joblocation=location)
    return render(request,"search.html",{'data':data})



def candprofile(request):
    if request.session['userid']:
        uid=request.session['userid']
        profiledata=tbl_candregistration.objects.get(id=uid)
    return render(request,"candidateprofile.html",{'profiledata':profiledata})









def compreg(request):
    msg=""
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        repassword=request.POST.get('cpassword')
        
        if password==repassword:
            if tbl_compregistration.objects.filter(remail=email):
                msg="E-mail already exist"
                return render(request,"companylogin.html",{'msg':msg})
            else:
                if tbl_compregistration.objects.filter(rpassword=password):
                    msg="Password already exist"
                    return render(request,"companylogin.html",{'msg':msg})
                else:
                    data=tbl_compregistration.objects.create(remail=email,rpassword=password,status=1)
                    data=tbl_complogin.objects.create(lemail=email,lpassword=password,status=1)
                    msg="Registration Successfully Done..."
                    return render(request,"companylogin.html",{'msg':msg})
        else:
            msg="Password not match...!!!"
    return render(request,"companylogin.html",{'msg':msg})






def complog(request):
    msg=""
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        if tbl_complogin.objects.filter(lemail=email,lpassword=password):
            data=tbl_compregistration.objects.get(remail=email,rpassword=password)
            request.session['userid']=data.id
            if data.status=='admin':
                return render(request,"companylogin.html",{'msg':msg})
            elif data.status=='1':
                return render(request,"companydetails.html",{'msg':msg,'login':'true'})

        else:
            msg="Incorrect Username or password"
            # return HttpResponse("incorrect username or password")
           

    return render(request,"companylogin.html",{'msg':msg})






def compdetails(request):
    
    msg=""
    if request.method=='POST':
        if request.session['userid']:
            uid=request.session['userid']
            title=request.POST.get('title')
            compname=request.POST.get('compname')
            compsite=request.POST.get('compsite')
            type=request.POST.get('type')
            location=request.POST.get('location')
            compdesc=request.POST.get('compdesc')
            qualification=request.POST.get('qualification')
            experience=request.POST.get('experience')
            link=request.POST.get('link')
            ldate=request.POST.get('ldate')
            data=tbl_compdetails.objects.create(complid=uid,jobtitle=title,companyname=compname,companysite=compsite,jobtype=type,joblocation=location,companydesc=compdesc,jobqualification=qualification, jobexperience=experience,joblink=link,jobldate=ldate,status=1)

    return render(request,"index.html",{})




def searchcand(request):

    if request.method=="POST":
        qualification=request.POST.get('qualification') 
        experience=request.POST.get('experience')
        datas=tbl_candregistration.objects.filter(qualification=qualification,experience=experience)   
    return render(request,"companydetails.html",{'datas':datas})


def compaccount(request):
    if request.session['userid']:
        uid=request.session['userid']
        accountdata=tbl_compregistration.objects.get(id=uid)
    return render(request,"companyaccount.html",{'accountdata':accountdata})


def createdjobs(request):
    if request.session['userid']:
        uid=request.session['userid']
        crjb=tbl_compdetails.objects.filter(complid=uid)
    return render(request,"companyaccount.html",{"crjb":crjb})



def deletejob(request,pk):
    if request.session['userid']:
        uid=request.session['userid']
        try:
            job=tbl_compdetails.objects.get(id=pk)
            job.delete()
            crjb=tbl_compdetails.objects.filter(complid=uid)
            return render(request,"companyaccount.html",{"crjb":crjb})
        except tbl_compdetails.DoesNotExist:
            crjb=tbl_compdetails.objects.filter(complid=uid)
            return render(request,"companyaccount.html",{"crjb":crjb})



            



    


