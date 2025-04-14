from django.contrib import admin
from workOrder.models import *

@admin.register(workOrder)
class  workOrderAdmin(admin.ModelAdmin):
    list_display = ('id','prismID','workOrderId','PO','Status','created_date')
    search_fields = ('id','prismID','workOrderId','PO','Status','created_date')
    list_filter = ('id','prismID','workOrderId','PO','Status','created_date')


class  authorizedBillingAdmin(admin.ModelAdmin):
    list_display = ('id','woID','itemID')
    search_fields = ('id','woID__prismID','woID__workOrderId','woID__PO')

class  internalPOAdmin(admin.ModelAdmin):
    list_display = ('id','poNumber')
    search_fields = ('id','poNumber')


class  internalPOAdmin(admin.ModelAdmin):
    list_display = ('id','poNumber')
    search_fields = ('id','poNumber')

class  DailyAdmin(admin.ModelAdmin):
    list_display = ('id','woID', 'crew', 'Location','Period','day')
    search_fields = ('id','woID__prismID','woID__workOrderId','woID__PO')

class DailyItemAdmin(admin.ModelAdmin):
    list_display = ('id','itemID','DailyID','invoice')
    search_fields = ('id','itemID__item__itemID', 'DailyID__woID__prismID','invoice')

class externalProductionAdmin(admin.ModelAdmin):
    list_display = ('id','woID',)
    search_fields = ('id','woID__prismID','woID__workOrderId','woID__PO')

class externalProdItemAdmin(admin.ModelAdmin):
    list_display = ('id','externalProdID','itemID')
    search_fields = ('id','externalProdID__woID__prismID','externalProdID__woID__workOrderId','externalProdID__woID__PO')

class employeeRecapAdmin(admin.ModelAdmin):
    search_fields = ('id','Period__id')

class DailyEmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','Status')
    search_fields = ('id','Status')
    list_filter = ('Status',)

class woInvoiceAdmin(admin.ModelAdmin):
    list_display = ('id','woID','estimateNumber','invoiceNumber','Status')
    search_fields = ('id','Status','invoiceNumber')
    list_filter = ('Status',)

class woEstimateAdmin(admin.ModelAdmin):
    list_display = ('id','woID','estimateNumber','Status')
    search_fields = ('id','Status','estimateNumber')
    list_filter = ('Status',)

class payrollAuditAdmin(admin.ModelAdmin):
    list_display = ('id','Location','Period','created_date')
    search_fields = ('id','Location','Period','created_date')
    list_filter = ('created_date',)


class itemAdmin(admin.ModelAdmin):
    list_display = ('itemID','name', 'description','is_new','created_date')
    search_fields = ('itemID','name', 'description','is_new','created_date')
    list_filter = ('itemID','name', 'description','is_new','created_date')


class itemPriceAdmin(admin.ModelAdmin):
    search_fields = ('item','location')
    list_filter = ('item','location')

class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ('employeeID','first_name','last_name')
    list_display = ('employeeID','first_name','last_name')

class DailyDocsAdmin(admin.ModelAdmin):
    list_display = ('id','Status', 'created_date')
    search_fields = ('id','Status', 'created_date')
    list_filter = ('Status','created_date')


admin.site.register(workOrderDuplicate)
admin.site.register(Locations)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(item, itemAdmin)
admin.site.register(itemPrice,itemPriceAdmin)
admin.site.register(payroll)
admin.site.register(payrollDetail)
admin.site.register(internalPO,internalPOAdmin)
admin.site.register(period)
admin.site.register(Daily, DailyAdmin)
admin.site.register(DailyEmployee, DailyEmployeeAdmin)
admin.site.register(DailyItem, DailyItemAdmin)
admin.site.register(DailyDocs, DailyDocsAdmin)
admin.site.register(employeeRecap, employeeRecapAdmin)
admin.site.register(woStatusLog)
admin.site.register(vendor)
admin.site.register(subcontractor)
admin.site.register(externalProduction, externalProductionAdmin)
admin.site.register(externalProdItem, externalProdItemAdmin)
admin.site.register(authorizedBilling, authorizedBillingAdmin)
admin.site.register(woEstimate, woEstimateAdmin)
admin.site.register(woInvoice, woInvoiceAdmin)
admin.site.register(employeeLocation)
admin.site.register(billingAddress)
admin.site.register(DailyAudit)
admin.site.register(payrollAudit, payrollAuditAdmin)
admin.site.register(logInAudit)
admin.site.register(woCommentLog)
admin.site.register(woAdjustment)
