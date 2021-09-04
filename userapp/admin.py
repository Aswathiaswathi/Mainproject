from django.contrib import admin
from userapp.models import *

# Register your models here.
admin.site.register(tbl_candregistration)
admin.site.register(tbl_candlogin)

admin.site.register(tbl_compregistration)
admin.site.register(tbl_complogin)

admin.site.register(tbl_compdetails)