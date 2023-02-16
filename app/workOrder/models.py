from contextlib import nullcontext
from operator import truediv
from pyexpat import model
from random import choices
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime
# Create your models here.

status_choice = (
    ('1', 'Not Started'),
    ('2', 'Work in Progress'),
    ('3', 'Pending Docs'),
    ('4', 'Pending Revised WO'),
    ('5', 'Invoiced'),
)

prodStatus_choice = (
    (1, 'Open'),
    (2, 'Estimated'),
    (3, 'Invoiced'),
)

estimateStatus_choice = (
    (1, 'Open'),
    (2, 'Closed')
)

class Locations(models.Model):
    LocationID = models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    employeeID = models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_initial = models.CharField(max_length=100, blank=True, null= True)
    supervisor_name = models.ForeignKey('self', blank=True, null=True,on_delete=models.SET_NULL, db_column='supervisor_name')
    termination_date = models.CharField(max_length=200, blank=True, null= True)
    hire_created =  models.CharField(max_length=200, blank=True, null= True)
    hourly_rate = models.CharField(max_length=200, blank=True, null= True)
    email = models.CharField(max_length=200, blank=True, null= True)
    Location = models.ForeignKey(Locations, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL, db_column='user')
    is_active = models.BooleanField(default=True)
    is_supervisor = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superAdmin = models.BooleanField(default=False)
    accounts_payable = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + ", " + self.last_name

class workOrder(models.Model):
    prismID = models.CharField(max_length=200)
    workOrderId= models.CharField(max_length=200)
    PO = models.CharField(max_length=200)
    POAmount	= models.CharField(max_length=200, blank=True, null=True)
    ConstType	= models.CharField(max_length=200, blank=True, null=True)
    ConstCoordinator= models.CharField(max_length=200, blank=True, null=True)	
    WorkOrderDate= models.CharField(max_length=200, blank=True, null=True)
    EstCompletion= models.CharField(max_length=200, blank=True, null=True)	
    IssuedBy= models.CharField(max_length=200, blank=True, null=True)	
    JobName	= models.CharField(max_length=200, blank=True, null=True)
    JobAddress	= models.CharField(max_length=200, blank=True, null=True)
    SiteContactName	= models.CharField(max_length=200, blank=True, null=True)
    SitePhoneNumber	= models.CharField(max_length=200, blank=True, null=True)
    Comments	= models.CharField(max_length=200, blank=True, null=True)
    Status	= models.CharField(max_length=20, blank=True, null=True, choices = status_choice)
    CloseDate	= models.CharField(max_length=200, blank=True, null=True)
    WCSup	= models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, db_column='WCSup')
    UploadDate	= models.CharField(max_length=200, blank=True, null=True)
    UserName= models.CharField(max_length=200, blank=True, null=True)
    Location = models.ForeignKey(Locations, on_delete=models.SET_NULL, null=True, blank=True)
    uploaded = models.BooleanField(default=False)
    linkedOrder = models.CharField(max_length=600, null=True, blank=True)
    pre_invoice = models.CharField(max_length=200, null=True, blank=True)
    invoice = models.CharField(max_length=200, null=True, blank=True)
    created_date = models.DateTimeField(blank=True, null=True)
    createdBy = models.CharField(max_length=60, blank=True, null=True)
    

    class Meta:
        unique_together = ('prismID', 'workOrderId','PO')

    def __str__(self):
        return self.prismID + " - " + self.workOrderId + " - " + self.PO
        
    @property
    def date_diff(self):
        return (5)

class workOrderDuplicate(models.Model):
    prismID = models.CharField(max_length=200, blank=True, null=True)
    workOrderId= models.CharField(max_length=200, blank=True, null=True)
    PO = models.CharField(max_length=200, blank=True, null=True)
    POAmount	= models.CharField(max_length=200, blank=True, null=True)
    ConstType	= models.CharField(max_length=200, blank=True, null=True)
    ConstCoordinator= models.CharField(max_length=200, blank=True, null=True)	
    WorkOrderDate= models.CharField(max_length=200, blank=True, null=True)
    EstCompletion= models.CharField(max_length=200, blank=True, null=True)	
    IssuedBy= models.CharField(max_length=200, blank=True, null=True)	
    JobName	= models.CharField(max_length=200, blank=True, null=True)
    JobAddress	= models.CharField(max_length=200, blank=True, null=True)
    SiteContactName	= models.CharField(max_length=200, blank=True, null=True)
    SitePhoneNumber	= models.CharField(max_length=200, blank=True, null=True)
    Comments	= models.CharField(max_length=200, blank=True, null=True)
    Status	= models.CharField(max_length=200, blank=True, null=True)
    CloseDate	= models.CharField(max_length=200, blank=True, null=True)
    WCSup	= models.CharField(max_length=200, blank=True, null=True)
    UploadDate	= models.CharField(max_length=200, blank=True, null=True)
    UserName= models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        unique_together = ('prismID',
        'workOrderId',
        'PO',
        'POAmount')

    def __str__(self):
        return self.prismID + " - " + self.PO + " - " + self.POAmount


class item(models.Model):
    itemID= models.CharField(primary_key=True, max_length=30, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True) 
    created_date = models.DateField()
    createdBy = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return self.itemID + " - " + self.name

class itemPrice(models.Model):
    item = models.ForeignKey(item, on_delete=models.CASCADE, db_column='item')
    location = models.ForeignKey(Locations, on_delete=models.CASCADE, db_column='location')
    pay_perc = models.CharField(max_length=20, blank=True, null=True)
    price = models.CharField(max_length=20, blank=True, null=True)
    emp_payout = models.CharField(max_length=200, blank=True, null=True)
    rate = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        unique_together = ('item', 'location')
    
    def __str__(self):
        return str(self.item) + " - " + str(self.location)


class payroll(models.Model):
    # location = models.ForeignKey(Locations, on_delete=models.CASCADE, db_column='location')
    # employee = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='employee')
    location = models.CharField(max_length=200)
    employee = models.CharField(max_length=200)
    date =  models.CharField(max_length=200)
    prismID = models.CharField(max_length=200)
    workOrderId= models.CharField(max_length=200)
    PO = models.CharField(max_length=200)
    RT = models.CharField(max_length=200, blank=True, null=True)
    OT = models.CharField(max_length=200, blank=True, null=True)
    DT = models.CharField(max_length=200, blank=True, null=True)
    IT = models.CharField(max_length=200, blank=True, null=True)
    RTPrice = models.CharField(max_length=200, blank=True, null=True)
    OTPrice = models.CharField(max_length=200, blank=True, null=True)
    bonus = models.CharField(max_length=200, blank=True, null=True)
    production = models.CharField(max_length=200, blank=True, null=True)
    ownVehicle = models.CharField(max_length=200, blank=True, null=True)
    onCall = models.CharField(max_length=200, blank=True, null=True)
    payroll = models.CharField(max_length=200, blank=True, null=True)
    supervisor = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    itemTotal = models.CharField(max_length=200, blank=True, null=True)
    invoice = models.CharField(max_length=200, blank=True, null=True)
    pdfDaily = models.CharField(max_length=800, blank=True, null=True)
    woId = models.ForeignKey(workOrder, on_delete=models.SET_NULL, db_column='woId', blank=True, null=True)

    class Meta:
            unique_together = ('location', 'employee', 'date', 'prismID', 'workOrderId','PO')


class payrollDetail(models.Model):
    # location = models.ForeignKey(Locations, on_delete=models.CASCADE, db_column='location')
    # employee = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='employee')
    location = models.CharField(max_length=200)
    employee = models.CharField(max_length=200)
    date =  models.CharField(max_length=200)
    prismID = models.CharField(max_length=200)
    workOrderId= models.CharField(max_length=200)
    PO = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)

    class Meta:
            unique_together = ('location', 'employee', 'date', 'prismID','workOrderId','PO', 'item')

        
class period(models.Model):
    periodID = models.IntegerField(null=False, blank=False)
    periodYear = models.IntegerField(null=False, blank=False)
    fromDate = models.DateField()
    toDate = models.DateField()
    payDate = models.DateField()
    weekRange = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField()
    approved_date = models.DateTimeField(null=True, blank=True)
    approvedBy = models.CharField(max_length=60, blank=True, null=True)
    closed_date = models.DateTimeField(null=True, blank=True)
    closedBy = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return str(self.periodID) + " - " + str(self.periodYear)

class Daily(models.Model):
    crew = models.IntegerField(null=False, blank=False)
    Location = models.ForeignKey(Locations, on_delete=models.CASCADE, db_column ='Location', null=False, blank=False)
    Period = models.ForeignKey(period, on_delete=models.CASCADE, db_column ='Period', null=False, blank=False)
    day = models.DateField(null=False, blank=False)
    woID = models.ForeignKey(workOrder, on_delete=models.CASCADE, db_column ='woID', null=True, blank=True)
    supervisor = models.CharField(max_length=200, blank=True, null=True)
    own_vehicle = models.FloatField(blank=True, null=True)
    total_pay = models.IntegerField(null=True, blank=True)
    split_paymet = models.BooleanField(default=False)
    pdfDaily = models.FileField(null=True, upload_to="dailys") 
    created_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.Period) + " - " + str(self.day)
    
    class Meta:
        unique_together = ('Period','Location','day', 'crew')

class DailyEmployee(models.Model):
    DailyID = models.ForeignKey(Daily, on_delete=models.CASCADE, db_column ='DailyID', null=False, blank=False)
    EmployeeID = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column ='EmployeeID', null=False, blank=False)
    per_to_pay =  models.FloatField(null=True, blank=True)
    on_call = models.FloatField(null=True, blank=True)
    bonus =  models.FloatField(null=True, blank=True)
    start_time = models.IntegerField(null=True, blank=True)
    start_lunch_time = models.IntegerField(null=True, blank=True)
    end_lunch_time = models.IntegerField(null=True, blank=True)
    end_time = models.IntegerField(null=True, blank=True)
    total_hours = models.FloatField(null=True, blank=True)
    regular_hours = models.FloatField(null=True, blank=True)
    ot_hour = models.FloatField(null=True, blank=True)
    double_time = models.FloatField(null=True, blank=True)
    payout =  models.FloatField(null=True, blank=True)
    created_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.DailyID) + " - " + str(self.EmployeeID)
    
    class Meta:
        unique_together = ('DailyID','EmployeeID')

class DailyItem(models.Model):
    DailyID = models.ForeignKey(Daily, on_delete=models.CASCADE, db_column ='DailyID', null=False, blank=False)
    itemID = models.ForeignKey(itemPrice, on_delete=models.CASCADE, db_column ='itemID', null=False, blank=False )
    quantity = models.IntegerField(null=False, blank=False)
    total = models.FloatField(null=True, blank=True)       
    estimate = models.CharField(max_length=50, null=True, blank=True)
    invoice = models.CharField(max_length=50, null=True, blank=True)
    Status = models.IntegerField(default=1, choices = prodStatus_choice)
    created_date = models.DateTimeField(null=True, blank=True) 

    def __str__(self):
        return str(self.DailyID) + " - " + str(self.itemID)
    
    class Meta:
        unique_together = ('DailyID','itemID')


class employeeRecap(models.Model):
    Period = models.ForeignKey(period, on_delete=models.CASCADE, db_column ='Period', null=False, blank=False)
    EmployeeID = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column ='EmployeeID', null=False, blank=False)
    recap = models.FileField(null=True, upload_to="Recaps")  
    mailingDate = models.DateTimeField(null=True, blank=True)    

    def __str__(self):
        return str(self.Period) + " - " + str(self.EmployeeID)
    
    class Meta:
        unique_together = ('Period','EmployeeID')    

class woStatusLog(models.Model):
    woID = models.ForeignKey(workOrder, on_delete=models.CASCADE, db_column ='woID')
    currentStatus = models.CharField(max_length=20, blank=True, null=True, choices = status_choice)
    nextStatus = models.CharField(max_length=20, blank=True, null=True, choices = status_choice)
    created_date = models.DateTimeField(blank=True, null=True)
    createdBy = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return str(self.woID) + " - " + str(self.currentStatus)


class vendor(models.Model):   
    name = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    contact = models.CharField(max_length=100, blank=True, null=True)
    contactPosition = models.CharField(max_length=100, blank=True, null=True)
    contactPhone = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(blank=True, null=True)
    createdBy = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return "V" + str(self.id) + " - " + str(self.name)

class subcontractor(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    contact = models.CharField(max_length=100, blank=True, null=True)
    contactPosition = models.CharField(max_length=100, blank=True, null=True)
    contactEmail = models.EmailField(max_length=100, blank=True, null=True)
    contactPhone = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(blank=True, null=True)
    createdBy = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return "S" +  str(self.id) + " - " + str(self.name)

class internalPO(models.Model):
    woID = models.ForeignKey(workOrder, on_delete=models.CASCADE, db_column ='woID')
    #vendor = models.ForeignKey(vendor, on_delete=models.SET_NULL, null=True, blank=True, db_column='vendor')
    vendor = models.CharField(max_length=50, null=True, blank=True)
    supervisor = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, db_column='supervisor', related_name='supervisor')
    pickupEmployee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, db_column='pickupEmployee', related_name='pickupEmployee')
    product = models.CharField(max_length=600, blank=True, null=True)
    quantity = models.CharField(max_length=20, blank=True, null=True)
    total = models.CharField(max_length=20, blank=True, null=True)
    nonBillable = models.BooleanField(default=False)
    estimate = models.CharField(max_length=50, null=True, blank=True)
    invoice = models.CharField(max_length=50, null=True, blank=True)
    Status = models.IntegerField(default=1, choices = prodStatus_choice)
    receipt = models.FileField(null=True, upload_to="po")

    class Meta:
        unique_together = ('id', 'woID')

    def __str__(self):
        return str(self.woID) + " - " + str(self.id)

class externalProduction(models.Model):
    woID = models.ForeignKey(workOrder, on_delete=models.CASCADE, db_column ='woID')
    subcontractor = models.ForeignKey(subcontractor, on_delete=models.SET_NULL, null=True, blank=True,  db_column ='subcontractor')
    invoiceNumber = models.CharField(max_length=60, blank=True, null=True)    
    invoice = models.FileField(null=True, upload_to="external_invoice")
    total_invoice = models.FloatField(blank=True, null=True)
    invoice_date = models.DateField(null=True, blank=True)
    created_date = models.DateTimeField(null=True, blank=True)
    createdBy = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return str(self.woID) + " - " + str(self.id)


class externalProdItem(models.Model):    
    externalProdID = models.ForeignKey(externalProduction, on_delete=models.CASCADE, db_column ='externalProdID')
    itemID = models.ForeignKey(itemPrice, on_delete=models.CASCADE, db_column ='itemID', null=False, blank=False )
    quantity = models.IntegerField(null=False, blank=False) 
    total = models.FloatField(null=True, blank=True)
    estimate = models.CharField(max_length=50, null=True, blank=True)
    invoice = models.CharField(max_length=50, null=True, blank=True)
    Status = models.IntegerField(default=1, choices = prodStatus_choice)
    created_date = models.DateTimeField(null=True, blank=True)
    createdBy = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return str(self.externalProdID) + " - " + str(self.id)

class authorizedBilling(models.Model):    
    woID = models.ForeignKey(workOrder, on_delete=models.CASCADE, db_column ='woID')
    itemID = models.ForeignKey(itemPrice, on_delete=models.CASCADE, db_column ='itemID', null=False, blank=False )
    quantity = models.IntegerField(null=False, blank=False) 
    total = models.FloatField(null=True, blank=True)
    estimate = models.CharField(max_length=50, null=True, blank=True)
    invoice = models.CharField(max_length=50, null=True, blank=True)
    Status = models.IntegerField(default=1, choices = prodStatus_choice)
    created_date = models.DateTimeField(null=True, blank=True)
    createdBy = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return str(self.woID) + " - " + str(self.id)
 
class woEstimate(models.Model):
    woID = models.ForeignKey(workOrder, on_delete=models.CASCADE, db_column ='woID')
    estimateNumber = models.IntegerField()
    total = models.FloatField(null=True, blank=True)
    Status = models.IntegerField(default=1, choices = estimateStatus_choice)
    is_partial = models.BooleanField(default=False)
    created_date = models.DateTimeField(null=True, blank=True)
    createdBy = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return str(self.woID) + " - " + str(self.id)

class woInvoice(models.Model):
    woID = models.ForeignKey(workOrder, on_delete=models.CASCADE, db_column ='woID')
    invoiceNumber = models.IntegerField()
    total = models.FloatField(null=True, blank=True)
    Status = models.IntegerField(default=1, choices = estimateStatus_choice)
    is_partial = models.BooleanField(default=False)
    created_date = models.DateTimeField(null=True, blank=True)
    createdBy = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return str(self.woID) + " - " + str(self.id)