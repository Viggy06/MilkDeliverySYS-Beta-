from django.contrib import admin
from .models import FixedForAll, Delivery_Boy_Model, OrderHistory, Dboyride

# Register your models here.
@admin.register(FixedForAll)
class A_FixedForAll(admin.ModelAdmin):
    list_display = ['CustomerID', 'Customer_Name', 'Address', 'Phone_No',
                    'Plan', 'Total_milk', 'Company_name', 'Group', 'dboy', 'status', 'bottles','remaining_bottles']

@admin.register(Delivery_Boy_Model)
class A_Delivery_Boy_Model(admin.ModelAdmin):
    list_display = ['DName', 'DLast_Name', 'Dusername', 'Dgender', 'Dage',
                    'DPhone_Number', 'DLocation', 'Demail', 'Dpassword','group','order']

@admin.register(OrderHistory)
class A_OrderHistory(admin.ModelAdmin):
    list_display = ['CustomerID','Customer_Name','Address','Phone_No','Plan','Total_milk','Company_name','DeliveryBoy','Ddate','ogroup','status','bottles','remaining_bottles','cust_comment']

@admin.register(Dboyride)
class A_Dboyride(admin.ModelAdmin):
    list_display = ['id','Dusername','Ddate','startride','endride','totalride']