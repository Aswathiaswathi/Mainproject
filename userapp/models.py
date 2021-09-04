from django.db import models

# Create your models here.
class tbl_candregistration(models.Model):
    fname=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    phone_no=models.IntegerField(null=True)
    qualification=models.CharField(max_length=50)
    experience=models.CharField(max_length=50)
    cv=models.CharField(max_length=200,null=True)
    status=models.CharField(max_length=10,default="")





class tbl_candlogin(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    status=models.CharField(max_length=10,default="")




class tbl_compregistration(models.Model):
    remail=models.EmailField(max_length=50)
    rpassword=models.CharField(max_length=50)
    status=models.CharField(max_length=10,default="")

class tbl_complogin(models.Model):
    lemail=models.EmailField(max_length=50)
    lpassword=models.CharField(max_length=50)
    status=models.CharField(max_length=10,default="")




class tbl_compdetails(models.Model):
    complid=models.CharField(max_length=10,default="",null=True)
    jobtitle=models.CharField(max_length=50)
    companyname=models.CharField(max_length=50)
    companysite=models.CharField(max_length=50)
    jobtype=models.CharField(max_length=50)
    joblocation=models.CharField(max_length=50)
    companydesc=models.CharField(max_length=500)
    jobqualification=models.CharField(max_length=50)
    jobexperience=models.CharField(max_length=50,null=True)
    joblink=models.CharField(max_length=50)
    jobldate=models.CharField(max_length=50, null=True)
    status=models.CharField(max_length=10,default="")



class tbl_jobsearch(models.Model):
    jtitle=models.CharField(max_length=50)
    jlocation=models.CharField(max_length=50)
    status=models.CharField(max_length=10,default="")


class tbl_candsearch(models.Model):
    qualification=models.CharField(max_length=10)
    experience=models.CharField(max_length=10)
    status=models.CharField(max_length=10,default="")

