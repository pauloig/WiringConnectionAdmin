from ast import Try, parse
from django.shortcuts import render, redirect
from django.http import HttpResponse
import xlwt
from datetime import datetime
from django.contrib.auth import authenticate, login as login_process
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from .models import *
from .forms import * 
from . import views
from sequences import get_next_value, Sequence
from workOrder import models as catalogModel
from datetime import datetime, timedelta


@login_required(login_url='/home/')
def mobile_home(request):
    emp =  catalogModel.Employee.objects.filter(user__username__exact = request.user.username).first()
    per = catalogModel.period.objects.filter(status=1).first()
    context ={}
    context["period"] = per    
    context["emp"]= emp
    

    #Select the location
    loca = catalogModel.Locations.objects.filter(LocationID = emp.Location.LocationID).first()
    context["selectedLocation"] = emp.Location.LocationID

    #getting the list of days per week
    startDate = per.fromDate
    numDays = 7
    week1 = []

    for x in range(0,numDays):
        selectedDay = False
        fullDate = startDate + timedelta(days = x)
        shortDate = fullDate.strftime("%a") + ' ' + fullDate.strftime("%d")
        longDate = fullDate.strftime("%A") + ' ' + fullDate.strftime("%d")
        day = fullDate.strftime("%d")
        """if dID == day:
            selectedDay = True
            selectedDate = fullDate
            twTitle += ' - ' + fullDate.strftime("%A").upper() + ', ' + fullDate.strftime("%B %d, %Y").upper()"""
        
        #obtengo la cantidad de Items asociados
        dItems = DailyMob.objects.filter(Period = per, Location = loca, day = fullDate)
        totalItems = 0

        for d in dItems:
            dItemDetail = DailyMobItem.objects.filter(DailyID=d)

            for i in dItemDetail:
                totalItems += i.quantity

        week1.append({'day':day, 'shortDate': shortDate, 'longDate': longDate, 'fullDate': fullDate, 'Total': totalItems, 'selected': selectedDay })

    startDate += timedelta(days = numDays)
    week2 = []
    for x in range(0,numDays):
        selectedDay = False
        fullDate = startDate + timedelta(days = x)
        shortDate = fullDate.strftime("%a") + ' ' + fullDate.strftime("%d")
        longDate = fullDate.strftime("%A") + ' ' + fullDate.strftime("%d")
        day = fullDate.strftime("%d")

        """if dID == day:
            selectedDay = True
            selectedDate = fullDate
            twTitle += ' - ' + fullDate.strftime("%A").upper() + ', ' + fullDate.strftime("%B %d, %Y").upper()"""

        #obtengo la cantidad de Items asociados
        dItems = DailyMob.objects.filter(Period = per, Location = loca, day = fullDate)
        totalItems = 0

        for d in dItems:
            dItemDetail = DailyMobItem.objects.filter(DailyID=d)

            for i in dItemDetail:
                totalItems += i.quantity

        week2.append({'day':day, 'shortDate': shortDate, 'longDate': longDate, 'fullDate': fullDate, 'Total': totalItems, 'selected': selectedDay })
    

    context["week1"] = week1
    context["week2"] = week2

    return render(request, "mobile/home.html", context)

@login_required(login_url='/home/')
def crew(request, perID, dID, crewID, LocID):
    emp =  catalogModel.Employee.objects.filter(user__username__exact = request.user.username).first()
    context ={}

    per = catalogModel.period.objects.filter(status__in=(1,2)).first()
    context["per"] = per    
    context["period"] = per    
    context["emp"]= emp

    #Select the location
    loca = catalogModel.Locations.objects.filter(LocationID = emp.Location.LocationID).first()

    twTitle = ''

    #getting the list of days per week
    startDate = per.fromDate
    numDays = 7
    week1 = []
    for x in range(0,numDays):
        selectedDay = False
        fullDate = startDate + timedelta(days = x)
        shortDate = fullDate.strftime("%a") + ' ' + fullDate.strftime("%d")
        longDate = fullDate.strftime("%A") + ' ' + fullDate.strftime("%d")
        day = fullDate.strftime("%d")
        if dID == day:
            selectedDay = True
            selectedDate = fullDate
            twTitle +=  fullDate.strftime("%A").upper() + ', ' + fullDate.strftime("%B %d, %Y").upper()
        
        #obtengo la cantidad de Items asociados
        dItems = DailyMob.objects.filter(Period = per, Location = loca, day = fullDate)
        totalItems = 0

        for d in dItems:
            dItemDetail = DailyMobItem.objects.filter(DailyID=d)

            for i in dItemDetail:
                totalItems += i.quantity

        week1.append({'day':day, 'shortDate': shortDate, 'longDate': longDate, 'fullDate': fullDate, 'Total': totalItems, 'selected': selectedDay })

    startDate += timedelta(days = numDays)
    week2 = []
    for x in range(0,numDays):
        selectedDay = False
        fullDate = startDate + timedelta(days = x)
        shortDate = fullDate.strftime("%a") + ' ' + fullDate.strftime("%d")
        longDate = fullDate.strftime("%A") + ' ' + fullDate.strftime("%d")
        day = fullDate.strftime("%d")

        if dID == day:
            selectedDay = True
            selectedDate = fullDate
            twTitle +=  fullDate.strftime("%A").upper() + ', ' + fullDate.strftime("%B %d, %Y").upper()

        #obtengo la cantidad de Items asociados
        dItems = DailyMob.objects.filter(Period = per, Location = loca, day = fullDate)
        totalItems = 0

        for d in dItems:
            dItemDetail = DailyMobItem.objects.filter(DailyID=d)

            for i in dItemDetail:
                totalItems += i.quantity

        week2.append({'day':day, 'shortDate': shortDate, 'longDate': longDate, 'fullDate': fullDate, 'Total': totalItems, 'selected': selectedDay })
    
    

    if request.user.is_staff or emp.is_superAdmin:
        superV = catalogModel.Employee.objects.filter(is_supervisor=True)
    else:
        superV = catalogModel.Employee.objects.filter(is_supervisor=True)

    if dID != "0":
        # get the list of dailys for the period, Day selected and Location
        crews = DailyMob.objects.filter(Period = perID, day=selectedDate, Location = loca).order_by('crew')
        context["crew"] = crews

    if crews.count() == 1:
        crewID = crews.first().crew

    if crewID != "0":
        dailyID = DailyMob.objects.filter(Period = perID, day=selectedDate, crew = crewID, Location = loca ).first()
        dailyEmp = DailyMobEmployee.objects.filter(DailyID = dailyID).order_by('created_date')
        context["dailyEmp"] = dailyEmp

        dailyItem = DailyMobItem.objects.filter(DailyID = dailyID).order_by('created_date')
        dailyTotal = 0
        ovT = 0
        for di in dailyItem:
            dailyTotal += di.total 


        if dailyID.own_vehicle != None:
            ovT = (dailyTotal * dailyID.own_vehicle) / 100
        
        granTotal = dailyTotal + ovT

        context["dailyItem"] = dailyItem
        context["TotalItem"] = dailyTotal
        context["ovTotal"] = ovT
        context["GranTotalItem"] = granTotal

    context["week1"] = week1
    context["week2"] = week2
    context["selectedDate"] = twTitle
    context["superV"] = superV
    context["selectedCrew"] = int(crewID)
    context["selectedDay"] = int(dID)
    context["selectedLocation"] = LocID

    return render(request, "mobile/crew.html", context)


@login_required(login_url='/home/')
def update_supervisor(request, perID, dID, crewID, LocID):
    emp =  catalogModel.Employee.objects.filter(user__username__exact = request.user.username).first()
    context ={}

    per = catalogModel.period.objects.filter(status__in=(1,2)).first()
    context["per"] = per    
    context["period"] = per    
    context["emp"]= emp

    if request.user.is_staff or emp.is_superAdmin:
        superV = catalogModel.Employee.objects.filter(is_supervisor=True)
    else:
        superV = catalogModel.Employee.objects.filter(is_supervisor=True)
    

    if request.method == 'POST':
        dailyID = request.POST.get('daily')
        sup = request.POST.get('supervisor') 
        split = request.POST.get('split')
        ptp = request.POST.get('ptp')
        ov = request.POST.get('ov')
        crew = DailyMob.objects.filter(id = dailyID).first()
        if crew:            
            crew.supervisor = sup                      
            crew.split_paymet = bool(split)   

            if ov != '':
                crew.own_vehicle = ov
            else:
                crew.own_vehicle = None    

            #emp_ptp = update_ptp_Emp(dailyID, bool(split))
            emp_ptp = 0

            crew.total_pay = emp_ptp     
            crew.save()
            per = crew.Period.id  

            #emp_ptp = update_ptp_Emp(dailyID, bool(split))       
            
            if int(str(sup))>0 and crew.woID != None:
                super = catalogModel.Employee.objects.filter(employeeID = sup ).first()
                if super:   
                    wo = catalogModel.workOrder.objects.filter( id = crew.woID.id).first()
                    if wo:             
                        wo.WCSup = super
                        wo.save()           

        return HttpResponseRedirect('/mobile/crew/' + str(per) + '/' + dID  + '/'+ str(crew.crew) +'/'+LocID)       

    context["superV"] = superV            
    context["selectedCrew"] = int(crewID)
    context["selectedDay"] = int(dID)
    context["selectedLocation"] = LocID      

    return render(request, "mobile/update_supervisor.html", context)


@login_required(login_url='/home/')
def create_daily(request, pID, dID, LocID):
    emp = catalogModel.Employee.objects.filter(user__username__exact = request.user.username).first()
    
    context = {}    
    context["emp"] = emp    
    per = catalogModel.period.objects.filter(id = pID).first()

    perActual = catalogModel.period.objects.filter(status__in=(1,2)).first()
    context["per"] = perActual

    if int(LocID) > 0:
        loc = catalogModel.Locations.objects.filter(LocationID = LocID).first()
    else:
        loc = catalogModel.Locations.objects.filter(LocationID = emp.Location.LocationID).first()

    if per:
        #Selecting the day date
        startDate = per.fromDate
        selectedDate = per.fromDate
        numDays = 14
        for x in range(0,numDays):            
            fullDate = startDate + timedelta(days = x)            
            day = fullDate.strftime("%d")
            if int(dID) == int(day):
                 selectedDate = fullDate

        crewNumber = DailyMob.objects.filter( Period = per, day = selectedDate, Location = loc).last()
        if crewNumber:
            crewNo = crewNumber.crew
        else:
            crewNo = 0

        crew  = DailyMob(
            Period = per,
            Location = loc,
            day = selectedDate,
            crew = int(crewNo) + 1,
            created_date = datetime.now()
        )

        crew.save()
        per = crew.Period.id
        
        #Adding Audit
        
        operationDetail = "Period: " + str(per) + ", Crew: " + str(crew.crew)       
        

        return HttpResponseRedirect('/mobile/crew/' + str(per) + '/' + crew.day.strftime("%d")  + '/'+ str(crew.crew) +'/'+LocID)
    else:
        return HttpResponseRedirect('/mobile/')

@login_required(login_url='/home/')
def delete_daily(request, id, LocID):
    emp = catalogModel.Employee.objects.filter(user__username__exact = request.user.username).first()
    context ={}
    per = catalogModel.period.objects.filter(status__in=(1,2)).first()
    context["per"] = per


    obj = get_object_or_404(DailyMob, id = id)
 
    context["form"] = obj
    context["emp"] = emp
 
 
    actual_wo = obj.woID
    
    obj.delete()

    if actual_wo != None:
        lastD = DailyMob.objects.filter(woID = actual_wo).last()
        wo = catalogModel.workOrder.objects.filter(id = actual_wo.id).first()
        
        if lastD:                 
            wo.UploadDate = lastD.created_date

            if lastD.supervisor != None:
                sup = catalogModel.Employee.objects.filter(employeeID = lastD.supervisor ).first()
                if sup:                
                    wo.WCSup = sup

            wo.save()
        else:             

            wo.Status = 1
            wo.Location = None
            wo.UploadDate = None
            wo.UserName = None
            wo.WCSup = None
            wo.UploadDate = datetime.now()
            wo.save()

        
    return HttpResponseRedirect('/mobile/crew/' + str(obj.Period.id) + '/' + obj.day.strftime("%d") + '/0/' + str(LocID)) 

@login_required(login_url='/home/')
def update_order_daily(request, woID, dailyID, LocID):
    emp = catalogModel.Employee.objects.filter(user__username__exact = request.user.username).first()

    context = {}    
    context["emp"] = emp    

    per = catalogModel.period.objects.filter(status__in=(1,2)).first()
    context["per"] = per

    crew = DailyMob.objects.filter(id = dailyID).first()
    wo = catalogModel.workOrder.objects.filter(id = woID).first()
    
    anterior = None

    if crew and wo:

        if crew.woID != None:
            anterior = catalogModel.workOrder.objects.filter(id = crew.woID.id).first()

            if anterior:                

                anterior.Status = 1
                anterior.Location = None
                anterior.UploadDate = None
                anterior.UserName = None
                anterior.WCSup = None
                anterior.UploadDate = datetime.now()
                anterior.save()


        crew.woID = wo
        crew.save()

        
        wo.Status = 2
        wo.Location = crew.Location
        wo.UploadDate = datetime.now()
        wo.UserName = request.user.username
        if crew.supervisor != None:
            sup = catalogModel.Employee.objects.filter(employeeID = crew.supervisor ).first()
            if sup:                
                wo.WCSup = sup

        wo.save()

        per = crew.Period.id
        
        #Adding Audit
        if crew.woID != None:            
            operationDetail = "Change on Selected WO - last WO: " + str(anterior) + ", New WO: " + str(wo)
        else:
            operationDetail = "Adding a Selected WO: " + str(wo)        

    return HttpResponseRedirect('/mobile/crew/' + str(per) + '/' + crew.day.strftime("%d")  + '/'+ str(crew.crew) +'/' + str(LocID))
    """"else:
        return HttpResponseRedirect('/mobile/')"""

@login_required(login_url='/home/')
def delete_daily_item(request, id, LocID):
    emp = catalogModel.Employee.objects.filter(user__username__exact = request.user.username).first()
    context ={}

    per = catalogModel.period.objects.filter(status__in=(1,2)).first()
    context["per"] = per

    obj = get_object_or_404(DailyMobItem, id = id)
 
    context["form"] = obj
    context["emp"] = emp
 
    if request.method == 'POST':
        
        operationDetail = "Deleting Item: " + str(obj.itemID) + ", Quantity: " + str(obj.quantity) + ", Total: " + str(obj.total)
        
        
        obj.delete()

        update_ptp_Emp(obj.DailyID.id, obj.DailyID.split_paymet) 

        return HttpResponseRedirect('/payroll/' + str(obj.DailyID.Period.id) + '/' + obj.DailyID.day.strftime("%d") + '/' + str(obj.DailyID.crew) +'/' + str(LocID)) 

   
    return render(request, "delete_daily_item.html", context)


@login_required(login_url='/home/')
def orders_payroll(request, dailyID, LocID):
    emp = catalogModel.Employee.objects.filter(user__username__exact = request.user.username).first()
    daily = DailyMob.objects.filter(id = dailyID).first()    
    loca = list(catalogModel.Locations.objects.all().exclude(LocationID = daily.Location.LocationID))
    
    WOdailyList = list(DailyMob.objects.filter(Period = daily.Period, day = daily.day, Location__LocationID = LocID).exclude(woID = None).values_list('woID__id',flat=True))


    wo = catalogModel.workOrder.objects.filter(Status__in = [1,2]).exclude(Location__in = loca).exclude(id__in = WOdailyList )
    context = {}    
    context["orders"] = wo
    context["emp"] = emp    
    context["daily"] = dailyID
    context["selectedLocation"] = LocID

    per = catalogModel.period.objects.filter(status__in=(1,2)).first()
    context["per"] = per
    #context["WOdailyList"] = WOdailyList

    return render(request, "mobile/orders_payroll.html", context)

@login_required(login_url='/home/')
def update_ptp_Emp(dailyID, split):
    emp_ptp = 0
    crew = DailyMob.objects.filter(id = dailyID).first()
    if crew:
        itemCount = 0
        itemSum = 0
        
        if bool(split):
            empCount = DailyMobEmployee.objects.filter(DailyID = crew).count()
           
            if empCount > 0:
                empPtp =  validate_decimals(100 / empCount)
                empList = DailyMobEmployee.objects.filter(DailyID = crew)

                for empl in empList:
                    empD = DailyMobEmployee.objects.filter(id = empl.id).first()
                    empD.per_to_pay = empPtp
                    empD.save()
      

        itemCount = DailyMobItem.objects.filter(DailyID = crew).count()
        if itemCount > 0:            
            itemList = DailyMobItem.objects.filter(DailyID = crew)

            for iteml in itemList:
                itemSum += iteml.total 

        if crew.own_vehicle != None:
            ovp = (itemSum * crew.own_vehicle) / 100
            itemSum += ovp                     
                                      
        empList = DailyMobEmployee.objects.filter(DailyID = crew)
        
        for empl in empList:
            rt_pay = 0
            ot_pay = 0
            dt_pay = 0
            empRate = 0
            production = 0
            
            empD = DailyMobEmployee.objects.filter(id = empl.id).first()    
            if empD.per_to_pay != None:                                         
                emp_ptp += empD.per_to_pay                 
            if itemCount > 0:
                pay_out = validate_decimals(((itemSum * empD.per_to_pay) / 100))
                production = validate_decimals(((itemSum * empD.per_to_pay) / 100))
            else: 
                if empD.EmployeeID.hourly_rate != None: 
                    empRate = validate_decimals(empD.EmployeeID.hourly_rate)

                rt_pay = (empD.regular_hours * empRate)
                ot_pay = (empD.ot_hour * (empRate * 1.5))
                dt_pay = (empD.double_time * (empRate * 2))
                pay_out = (empD.regular_hours * empRate) + (empD.ot_hour * (empRate * 1.5)) + (empD.double_time * (empRate * 2))

            if empD.on_call != None:
                pay_out += empD.on_call

            if empD.bonus != None:
                pay_out += empD.bonus
            
            empD.rt_pay = rt_pay
            empD.ot_pay = ot_pay
            empD.dt_pay = dt_pay
            empD.emp_rate = empRate
            empD.payout = pay_out
            empD.production = production
            empD.save()
        
        crew.total_pay = round(emp_ptp)
        crew.save()
    return emp_ptp

# ****************************************************************************
def employee_list(request):
    emp =  catalogModel.Employee.objects.filter(user__username__exact = request.user.username).first()
    context ={}

    
    context["dataset"] = Timesheet.objects.filter(EmployeeID = emp, Status__in = (1,5)).order_by('-date').values()
    
    context["emp"]= emp

    return render(request, "mobile/employee_list.html", context)

@login_required(login_url='/home/')
def employee_submitted_list(request):
    emp = catalogModel.Employee.objects.filter(user__username__exact = request.user.username).first()
    context ={}

    
    context["dataset"] = Timesheet.objects.filter(EmployeeID = emp, Status__in = (2,3,4)).order_by('-date').values()
    
    context["emp"]= emp

    return render(request, "mobile/employee_submitted_list.html", context)



@login_required(login_url='/home/')
def create(request):
    emp = catalogModel.Employee.objects.filter(user__username__exact = request.user.username).first()
    context ={}


    
    form = TimesheetForm(request.POST or None, initial = {'EmployeeID': emp})
    
    if form.is_valid():
        form.instance.createdBy = request.user.username
        form.instance.created_date = datetime.now()   

        if request.POST.get('newstatus') != '' :
            form.instance.Status = request.POST.get('newstatus')

        if request.POST.get('newTotalM') != '' :    
            form.instance.total_mileage = request.POST.get('newTotalM')
        else:
            form.instance.total_mileage = 0

        form.instance.total_mileage = validate_decimals(validate_decimals(form.cleaned_data["end_mileage"]) - validate_decimals(form.cleaned_data["start_mileage"]))
        form.instance.total_hours = calculate_hours(form.instance.start_time, form.instance.end_time, form.instance.start_lunch_time, form.instance.end_lunch_time)
        form.save() 

        # Return to Locations List
        return HttpResponseRedirect('/mobile/employee_list/')
       
 
    context['form']= form
    context["emp"] = emp
    return render(request, "mobile/timesheet.html", context)


@login_required(login_url='/home/')
def update(request, id):
    emp = catalogModel.Employee.objects.filter(user__username__exact = request.user.username).first()
    context ={}

    obj = get_object_or_404(Timesheet, id = id)

    if int(obj.Status) >= 2 and int(obj.Status) <= 4:
        form = TimesheetDisabledForm(request.POST or None, instance = obj)
    else: 
        form = TimesheetForm(request.POST or None, instance = obj)

    if form.is_valid():
        if request.POST.get('newstatus') != '' :
            form.instance.Status = request.POST.get('newstatus')

        form.instance.total_mileage = validate_decimals(validate_decimals(form.instance.end_mileage) - validate_decimals(form.instance.start_mileage))
        form.instance.total_hours = calculate_hours(form.instance.start_time, form.instance.end_time, form.instance.start_lunch_time, form.instance.end_lunch_time)
        form.instance.updatedBy = request.user.username
        form.instance.updated_date = datetime.now()    
        form.save()
        # Return to Locations List
        return HttpResponseRedirect('/mobile/employee_list/')

    context["object"] = obj     
    context['form']= form
    context["emp"] = emp
    context["id"] = id
    return render(request, "mobile/timesheet.html", context)


"""
**************** SUPERVISOR *********************************
"""

@login_required(login_url='/home/')
def supervisor_list(request):
    emp = catalogModel.Employee.objects.filter(user__username__exact = request.user.username).first()
    context ={}
    status = 0
    dateS = ""
    dateS2 = ""
    loc = "0"
    employee = "0"

    locationList = catalogModel.Locations.objects.all()
    empList = catalogModel.Employee.objects.all()


    if request.method == "POST":
        dateSelected =  request.POST.get('date')
        dateSelected2 = request.POST.get('date2')
        dateS = datetime.strptime(dateSelected, '%Y-%m-%d').date()
        dateS2 = datetime.strptime(dateSelected2, '%Y-%m-%d').date()
        status = request.POST.get('status')        
        loc = request.POST.get('location') 
        employee = request.POST.get('emp')

        if loc == None or loc =="":
            loc = "0"
        
        if emp == None or emp =="":
            emp = "0"
           
        if status == "0" and loc == "0" and employee == "0":
            ts = Timesheet.objects.filter(Status__in = (2,3), date__range=[dateS, dateS2])
        else:
            if status != "0" and loc != "0" and employee != "0":
                ts = Timesheet.objects.filter(Status = status, Location__LocationID = loc, EmployeeID__employeeID = employee, date__range=[dateS, dateS2])  
            else:
                if status != "0" and loc!= "0":    
                    ts = Timesheet.objects.filter(Status = status , Location__LocationID = loc, date__range=[dateS, dateS2])            
                else:    
                    if  status != "0" and employee != "0":
                        ts = Timesheet.objects.filter(Status = status , EmployeeID__employeeID = employee, date__range=[dateS, dateS2])   
                    else:
                        if  loc != "0" and employee != "0":
                            ts = Timesheet.objects.filter(Location__LocationID = loc, EmployeeID__employeeID = employee, date__range=[dateS, dateS2])   
                        else:
                            if status != "0":
                                ts = Timesheet.objects.filter(Status = status , date__range=[dateS, dateS2]) 
                            else:
                                if loc != "0":
                                    ts = Timesheet.objects.filter(Location__LocationID = loc, date__range=[dateS, dateS2]) 
                                else:
                                    ts = Timesheet.objects.filter(EmployeeID__employeeID = employee, date__range=[dateS, dateS2])  
    else:
        ts = Timesheet.objects.filter(Status__in = (2,3))
        
    context["emp"] = emp
    context["dataset"] = ts
    context["location"]=locationList
    context["empList"]=empList
    context["selectLoc"]=loc
    context["selectEstatus"] = status 
    context["selectEmployee"] = employee 
    context["dateSelected"] =  dateS
    context["dateSelected2"] =  dateS2


        
    return render(request, "mobile/supervisor_list.html", context)




@login_required(login_url='/home/')
def createBySupervisor(request):
    emp = catalogModel.Employee.objects.filter(user__username__exact = request.user.username).first()
    context ={}

    form = TimesheetSuperForm(request.POST or None)

    if form.is_valid():
        form.instance.createdBy = request.user.username
        form.instance.created_date = datetime.now()    
        form.instance.total_mileage = validate_decimals(validate_decimals(form.instance.end_mileage) - validate_decimals(form.instance.start_mileage))
        form.instance.total_hours = calculate_hours(form.instance.start_time, form.instance.end_time, form.instance.start_lunch_time, form.instance.end_lunch_time)
        form.save()
        # Return to Locations List
        return HttpResponseRedirect('/mobile/supervisor_list/')

         
    context['form']= form
    context["emp"] = emp
    return render(request, "mobile/supervisor_timesheet.html", context)

@login_required(login_url='/home/')
def update_status(request, id, status):
    emp = catalogModel.Employee.objects.filter(user__username__exact = request.user.username).first()
    context ={}

    obj = get_object_or_404(Timesheet, id = id)
    
    if obj:
        obj.updatedBy = request.user.username
        obj.updated_date = datetime.now()    
        obj.Status = status
        obj.save()
        # Return to Locations List
        return HttpResponseRedirect('/mobile/supervisor_list/')

        
    context["emp"] = emp
    context["id"] = id
    return render(request, "mobile/timesheet.html/" + str(id), context)

@login_required(login_url='/home/')
def updateBySuper(request, id):
    emp = catalogModel.Employee.objects.filter(user__username__exact = request.user.username).first()
    context ={}

    obj = get_object_or_404(Timesheet, id = id)

    if obj.Status == 4:
        form = TimesheetSuperFormApproved(request.POST or None, instance = obj)
    else:
        form = TimesheetSuperForm(request.POST or None, instance = obj)

    if form.is_valid():
    
        if request.POST.get('newstatus') != '' :
                form.instance.Status = request.POST.get('newstatus')

        form.instance.total_mileage = validate_decimals(validate_decimals(form.instance.end_mileage) - validate_decimals(form.instance.start_mileage))
        form.instance.total_hours = calculate_hours(form.instance.start_time, form.instance.end_time, form.instance.start_lunch_time, form.instance.end_lunch_time)

        form.instance.updatedBy = request.user.username
        form.instance.updated_date = datetime.now()    
        form.save()
        # Return to Locations List
        return HttpResponseRedirect('/mobile/supervisor_list/')

         
    context['obj']= obj
    context['form']= form
    context["emp"] = emp
    context["id"] = id
    return render(request, "mobile/supervisor_timesheet.html", context)


def reject_timesheet(request, id):
    emp = catalogModel.Employee.objects.filter(user__username__exact = request.user.username).first()
    context ={}

    obj = get_object_or_404(Timesheet, id = id)
    form = TimesheetRejectedForm(request.POST or None, instance = obj)
    
    if form.is_valid():
        form.instance.updatedBy = request.user.username
        form.instance.updated_date = datetime.now()    
        form.instance.Status = 5
        form.save()
        # Return to Locations List
        return HttpResponseRedirect('/mobile/supervisor_list/')

    context['form']= form     
    context["emp"] = emp
    context["id"] = id
    return render(request, "mobile/reject_timesheet.html", context)


def approve_timesheet(request, id):
    emp = catalogModel.Employee.objects.filter(user__username__exact = request.user.username).first()
    per = catalogModel.period.objects.filter(status__in=(1,2)).first()
    context ={}
    context["per"] = per

    obj = get_object_or_404(Timesheet, id = id)
    
    if obj:
        crew = DailyMob.objects.filter(Location = obj.Location, Period = per, day = obj.date)
    else:
        crew = None


    form = TimesheetApprovedForm(request.POST or None, instance = obj, qs = crew) 
    
    if form.is_valid():
        form.instance.tranferredBy = request.user.username
        form.instance.transferred_date = datetime.now()    
        form.instance.Status = 4
        form.save()

        # se agrega la timesheet al crew
        crew = DailyMob.objects.filter(Location = obj.Location, Period = per, day = obj.date, crew = form.instance.crew.crew).first()

        dailyemp = catalogModel.DailyEmployee(DailyID = crew,
                                              EmployeeID = form.instance.EmployeeID,
                                              start_time =  form.instance.start_time,
                                              start_lunch_time =form.instance.start_lunch_time,
                                              end_lunch_time = form.instance.end_lunch_time,
                                              end_time = form.instance.end_time,
                                              total_hours = form.instance.total_hours,
                                              Status = 1,
                                              created_date = datetime.now())
        dailyemp.save()

        # Return to Locations List
        return HttpResponseRedirect('/mobile/supervisor_list/')

    context['form']= form     
    context["emp"] = emp
    
    context["id"] = id
    return render(request, "mobile/approve_timesheet.html", context)

"""
****************  REPORTS *********************************
"""
@login_required(login_url='/home/')
def report_list(request):
    
    context ={}
    emp = catalogModel.Employee.objects.filter(user__username__exact = request.user.username).first()
    context["emp"]= emp

    status = 0
    dateS = ""
    dateS2 = ""
    loc = "0"
    employee = "0"
    radio = None

    locationList = catalogModel.Locations.objects.all()
    empList = catalogModel.Employee.objects.all()

    if request.method == "POST":
        dateSelected =  request.POST.get('date')
        dateSelected2 = request.POST.get('date2')
        dateS = datetime.strptime(dateSelected, '%Y-%m-%d').date()
        dateS2 = datetime.strptime(dateSelected2, '%Y-%m-%d').date()
        status = request.POST.get('status')   
        employee =  request.POST.get('emp') 
        radio = request.POST.get('searchBy')

        loc = request.POST.get('location') 
        
        if loc == None or loc =="":
            loc = "0"
        
        if emp == None or emp =="":
            emp = "0"

        if radio == "byWork":
            if status == "0" and loc == "0" and employee == "0":
                ts = Timesheet.objects.filter(Status__in = (2,3), date__range=[dateS, dateS2])
            else:
                if status != "0" and loc != "0" and employee != "0":
                    ts = Timesheet.objects.filter(Status = status, Location__LocationID = loc, EmployeeID__employeeID = employee, date__range=[dateS, dateS2])  
                else:
                    if status != "0" and loc!= "0":    
                        ts = Timesheet.objects.filter(Status = status , Location__LocationID = loc, date__range=[dateS, dateS2])            
                    else:    
                        if  status != "0" and employee != "0":
                            ts = Timesheet.objects.filter(Status = status , EmployeeID__employeeID = employee, date__range=[dateS, dateS2])   
                        else:
                            if  loc != "0" and employee != "0":
                                ts = Timesheet.objects.filter(Location__LocationID = loc, EmployeeID__employeeID = employee, date__range=[dateS, dateS2])   
                            else:
                                if status != "0":
                                    ts = Timesheet.objects.filter(Status = status , date__range=[dateS, dateS2]) 
                                else:
                                    if loc != "0":
                                        ts = Timesheet.objects.filter(Location__LocationID = loc, date__range=[dateS, dateS2]) 
                                    else:
                                        ts = Timesheet.objects.filter(EmployeeID__employeeID = employee, date__range=[dateS, dateS2])  
        elif radio == "byCreated":
            if status == "0" and loc == "0" and employee == "0":
                ts = Timesheet.objects.filter(Status__in = (2,3), created_date__date__range=[dateS, dateS2])
            else:
                if status != "0" and loc != "0" and employee != "0":
                    ts = Timesheet.objects.filter(Status = status, Location__LocationID = loc, EmployeeID__employeeID = employee, created_date__date__range=[dateS, dateS2])  
                else:
                    if status != "0" and loc!= "0":    
                        ts = Timesheet.objects.filter(Status = status , Location__LocationID = loc, created_date__date__range=[dateS, dateS2])            
                    else:    
                        if  status != "0" and employee != "0":
                            ts = Timesheet.objects.filter(Status = status , EmployeeID__employeeID = employee, created_date__date__range=[dateS, dateS2])   
                        else:
                            if  loc != "0" and employee != "0":
                                ts = Timesheet.objects.filter(Location__LocationID = loc, EmployeeID__employeeID = employee, created_date__date__range=[dateS, dateS2])   
                            else:
                                if status != "0":
                                    ts = Timesheet.objects.filter(Status = status , created_date__date__range=[dateS, dateS2]) 
                                else:
                                    if loc != "0":
                                        ts = Timesheet.objects.filter(Location__LocationID = loc, created_date__date__range=[dateS, dateS2]) 
                                    else:
                                        ts = Timesheet.objects.filter(EmployeeID__employeeID = employee, created_date__date__range=[dateS, dateS2])  
    else:
        ts = Timesheet.objects.filter(Status = -1)
        
    context["dataset"] = ts
    context["radio"] = radio
    context["location"]=locationList
    context["empList"]=empList
    context["selectLoc"]=loc
    context["selectEstatus"] = status 
    context["selectEmployee"] = employee 
    context["dateSelected"] =  dateS
    context["dateSelected2"] =  dateS2


    return render(request, "mobile/report_list.html", context)


@login_required(login_url='/home/')
def get_report_list(request, dateSelected, dateSelected2, status, location, employee, type):
    

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('employee-report', cell_overwrite_ok = True) 

    

    # Sheet header, first row
    row_num = 4

    font_title = xlwt.XFStyle()
    font_title.font.bold = True
    font_title = xlwt.easyxf('font: bold on, color black;\
                     borders: top_color black, bottom_color black, right_color black, left_color black,\
                              left thin, right thin, top thin, bottom thin;\
                     pattern: pattern solid, fore_color gray25;')

    
    font_style =  xlwt.XFStyle()              

    font_title2 = xlwt.easyxf('font: bold on, color black;\
                                align: horiz center;\
                                pattern: pattern solid, fore_color gray25;')

    dateS = datetime.strptime(dateSelected, '%Y-%m-%d').date()
    dateS2 = datetime.strptime(dateSelected2, '%Y-%m-%d').date()
    
                              
    ws.write_merge(3, 3, 0, 14, 'Employee Report ' + str(datetime.strftime(dateS, "%m/%d/%Y")) + ' - ' + str(datetime.strftime(dateS2, "%m/%d/%Y")),font_title2)   


                   

    columns = ['Date','Created Date' ,'Name', 'Location', 'Clock In', 'Lunch Start','Lunch End','Clock Out','Hours worked', 'Starting Mileage','Ending Mileage','Total Mileage','Status', 'Updated By', 'Comments' ] 

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_title) # at 0 row 0 column 
      

    
    #ordenes = woInvoice.objects.filter(created_date__year = datetime.strftime(dateS, '%Y'), created_date__month = datetime.strftime(dateS, '%m'))


    """if status == "0" and location == "0":
        ts = Timesheet.objects.filter(date__range=[dateS, dateS2])
    else:
        if status != "0" and location != "0":
            ts = Timesheet.objects.filter(Status = status, Location__LocationID = location, date__range=[dateS, dateS2])  
        else:
            if status != "0":    
                ts = Timesheet.objects.filter(Status = status , date__range=[dateS, dateS2])                     
            else:
                ts = Timesheet.objects.filter(Location__LocationID = location , date__range=[dateS, dateS2])  """


    if type =="byWork":      
        if status == "0" and location == "0" and employee == "0":
            ts = Timesheet.objects.filter(Status__in = (2,3), date__range=[dateS, dateS2])
        else:
            if status != "0" and location != "0" and employee != "0":
                ts = Timesheet.objects.filter(Status = status, Location__LocationID = location, EmployeeID__employeeID = employee, date__range=[dateS, dateS2])  
            else:
                if status != "0" and location!= "0":    
                    ts = Timesheet.objects.filter(Status = status , Location__LocationID = location, date__range=[dateS, dateS2])            
                else:    
                    if  status != "0" and employee != "0":
                        ts = Timesheet.objects.filter(Status = status , EmployeeID__employeeID = employee, date__range=[dateS, dateS2])   
                    else:
                        if  location != "0" and employee != "0":
                            ts = Timesheet.objects.filter(Location__LocationID = location, EmployeeID__employeeID = employee, date__range=[dateS, dateS2])   
                        else:
                            if status != "0":
                                ts = Timesheet.objects.filter(Status = status , date__range=[dateS, dateS2]) 
                            else:
                                if location != "0":
                                    ts = Timesheet.objects.filter(Location__LocationID = location, date__range=[dateS, dateS2]) 
                                else:
                                    ts = Timesheet.objects.filter(EmployeeID__employeeID = employee, date__range=[dateS, dateS2])  
    elif type=="byCreated":
        if status == "0" and location == "0" and employee == "0":
            ts = Timesheet.objects.filter(Status__in = (2,3), created_date__date__range=[dateS, dateS2])
        else:
            if status != "0" and location != "0" and employee != "0":
                ts = Timesheet.objects.filter(Status = status, Location__LocationID = location, EmployeeID__employeeID = employee, created_date__date__range=[dateS, dateS2])  
            else:
                if status != "0" and location!= "0":    
                    ts = Timesheet.objects.filter(Status = status , Location__LocationID = location, created_date__date__range=[dateS, dateS2])            
                else:    
                    if  status != "0" and employee != "0":
                        ts = Timesheet.objects.filter(Status = status , EmployeeID__employeeID = employee, created_date__date__range=[dateS, dateS2])   
                    else:
                        if  location != "0" and employee != "0":
                            ts = Timesheet.objects.filter(Location__LocationID = location, EmployeeID__employeeID = employee, created_date__date__range=[dateS, dateS2])   
                        else:
                            if status != "0":
                                ts = Timesheet.objects.filter(Status = status , created_date__date__range=[dateS, dateS2]) 
                            else:
                                if location != "0":
                                    ts = Timesheet.objects.filter(Location__LocationID = location, created_date__date__range=[dateS, dateS2]) 
                                else:
                                    ts = Timesheet.objects.filter(EmployeeID__employeeID = employee, created_date__date__range=[dateS, dateS2])  


       
    for item in ts:
        row_num += 1
        ws.write(row_num, 0, item.date.strftime("%m/%d/%Y"), font_style) # at 0 row 0 column 
        ws.write(row_num, 1, item.created_date.strftime("%m/%d/%Y"), font_style) # at 0 row 0 column 
        ws.write(row_num, 2, item.EmployeeID.first_name + ' ' + item.EmployeeID.last_name , font_style) # at 0 row 0 column  
        ws.write(row_num,3, item.Location.LocationID + '-' + item.Location.name, font_style) # at 0 row 0 column        
        ws.write(row_num, 4, item.start_time, font_style)
        ws.write(row_num, 5, item.start_lunch_time, font_style)
        ws.write(row_num, 6, item.end_lunch_time, font_style)
        ws.write(row_num, 7, item.end_time, font_style)
        ws.write(row_num, 8, item.total_hours, font_style)
        ws.write(row_num, 9, item.start_mileage, font_style)
        ws.write(row_num, 10, item.end_mileage, font_style)
        ws.write(row_num, 11, item.total_mileage, font_style)

        if item.Status == 1:
            ws.write(row_num, 12, 'Draft', font_style)
        elif item.Status == 2:
            ws.write(row_num, 12, 'Sent', font_style)
        elif item.Status == 3:
            ws.write(row_num, 12, 'Pending', font_style)
        elif item.Status == 4:
            ws.write(row_num, 12, 'Approved', font_style)
        elif item.Status == 5:
            ws.write(row_num, 12, 'Rejected', font_style)

        ws.write(row_num, 13, item.updatedBy, font_style)
        ws.write(row_num, 14, item.comments, font_style)
            


    ws.col(2).width = 12000
    ws.col(3).width = 6000
    ws.col(4).width = 3000
    ws.col(5).width = 3000
    ws.col(6).width = 3000
    ws.col(7).width = 3000
    ws.col(8).width = 4000
    ws.col(9).width = 4000
    ws.col(10).width = 4000
    ws.col(11).width = 7000
    ws.col(12).width = 6000
    ws.col(13).width = 3000
    ws.col(14).width = 8000
 

    filename = 'Employee report ' + dateSelected + '.xls'
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=' + filename 

    wb.save(response)

    return response

"""
****************  UTILITIES *********************************
"""
def validate_decimals(value):
    try:
        return round(float(str(value)), 2)
    except:
       return 0
    
def calculate_hours(startTime, endTime, lunch_startTime, lunch_endTime):
    
    if startTime != None and endTime != None:
        if startTime > endTime:
            total = 0
        else:
            #convert to decimal
            startTime = startTime/100
            st_h = int(startTime) 
            st_m = validate_decimals(startTime % 1)* 100
            st_total = validate_decimals(st_h + validate_decimals(st_m / 60))
            
            endTime = endTime / 100
            et_h = int(endTime) 
            et_m = validate_decimals(endTime % 1)* 100
            et_total = validate_decimals(et_h + validate_decimals(et_m / 60))
            
            total = et_total - st_total
    else:
        total = 0 
    
    if lunch_startTime != None and lunch_endTime != None:
        lunch_startTime = lunch_startTime / 100
        lunch_endTime = lunch_endTime / 100
        
        if lunch_startTime > lunch_endTime:
            total_lunch = 0
        elif lunch_startTime > endTime or lunch_endTime > endTime:
            total_lunch = 0
        else:
            #convert to decimal
            lst_h = int(lunch_startTime) 
            lst_m = validate_decimals(lunch_startTime % 1) * 100
            lst_total = validate_decimals(lst_h + validate_decimals(lst_m / 60))
            
            let_h = int(lunch_endTime) 
            let_m = validate_decimals(lunch_endTime % 1)* 100
            let_total = validate_decimals(let_h + validate_decimals(let_m / 60))
            
            total_lunch = let_total - lst_total
    else:
        total_lunch = 0
    
    endTotal = total - total_lunch

    return endTotal