from django.db import models

# Create your models here.

class Delivery_Boy_Model(models.Model):
    DName = models.CharField(max_length=50)
    DLast_Name = models.CharField(max_length=50)
    Dusername = models.CharField(max_length=30)
    Dgender = models.CharField(max_length=30)
    Dage = models.CharField(max_length=15)
    DPhone_Number = models.CharField(max_length=50)
    DLocation = models.CharField(max_length=50,null=True,blank=True)
    Demail = models.EmailField()
    Dpassword = models.CharField(max_length=30)
    group = models.CharField(max_length=255,null=True,blank=True)
    order = models.CharField(max_length=255,null=True,blank=True)
    status = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self) -> str:
        return self.Dusername

class FixedForAll(models.Model):
    CustomerID = models.CharField(max_length=255, primary_key=True, null=False, blank=False)
    Customer_Name = models.CharField(max_length=255,blank=True,null=True)
    Address = models.TextField(null=True,blank=True)
    Phone_No = models.CharField(max_length=255,null=True,blank=True)
    Plan = models.TextField(blank=True,null=True)
    Total_milk = models.CharField(max_length=255,blank=True, null=True)
    Company_name = models.CharField(max_length=255)
    Group = models.CharField(max_length=255, blank=True, null=True)
    dboy = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    bottles = models.IntegerField(null=True, blank=True)
    remaining_bottles = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.CustomerID

class OrderHistory(models.Model):
    CustomerID = models.CharField(max_length=255,null=False, blank=False) #!!!!!!
    Customer_Name = models.CharField(max_length=255,blank=True,null=True)
    Address = models.CharField(max_length=255,null=True,blank=True)
    Phone_No = models.CharField(max_length=255,null=True,blank=True)
    Plan = models.CharField(max_length=255,blank=True,null=True)
    Total_milk = models.CharField(max_length=255,blank=True, null=True)
    Company_name = models.CharField(max_length=255)

    DeliveryBoy = models.CharField('DeliveryBoy',max_length=100,blank=True)
    Ddate = models.CharField('Date',max_length=100)
    ogroup = models.CharField('Group Name',max_length=255)
    status = models.CharField('Delivery Status',max_length=100)
    bottles = models.IntegerField(null=True, blank=True)
    remaining_bottles = models.IntegerField(null=True, blank=True)
    cust_comment = models.CharField(max_length=255, blank=True, null=True)    

    class Meta:
        db_table = 'OrderHistory'

    def __str__(self):
        return self.CustomerID+" "+self.Customer_Name+" "+self.Address+" "+self.Phone_No+" "+self.Plan+" "+self.Total_milk+" "+self.Company_name+" "+self.DeliveryBoy+" "+self.Ddate+" "+self.ogroup+" "+self.status+" "+self.cust_comment

class Dboyride(models.Model):
    Dusername = models.CharField(max_length=30)
    Ddate = models.CharField('Date',max_length=100)
    startride = models.DecimalField(decimal_places=2 ,max_digits=5)
    endride = models.DecimalField(decimal_places=2 ,max_digits=5)
    totalride = models.DecimalField(decimal_places=2 ,max_digits=5)

    class Meta:
        db_table = 'Dboyride'
    
    def __str__(self):
         return self.Dusername+" "+self.Ddate+" "+str(self.startride)+" "+str(self.endride)+" "+str(self.totalride)