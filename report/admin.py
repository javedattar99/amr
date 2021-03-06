from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.

from .models import Report, Publisher, Category, Image, Lead, Billing_Details,Contact_Us


class CategoryAdmin(ImportExportActionModelAdmin):
    list_display = ['id', 'name', 'description', 'slug']


class PublisherAdmin(ImportExportActionModelAdmin):
    list_display = ['id', 'name', 'description', 'slug']


class ReportAdmin(ImportExportActionModelAdmin):
    list_display = ['id', 'title', 'category', 'publisher']
    list_filter = ('category', 'publisher')


class LeadAdmin(ImportExportActionModelAdmin):
    list_display = ['id', 'lead_date','report', 'full_name', 'corporate_email', 'country', 'phone', 'job_title', 'company',
                    'comment' ]

class ContactUsAdmin(ImportExportActionModelAdmin):
    list_display = ['id','full_name', 'corporate_email','phone','subject','message']


admin.site.register(Report,ReportAdmin)
admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Lead,LeadAdmin)
admin.site.register(Image)
admin.site.register(Billing_Details)
admin.site.register(Contact_Us,ContactUsAdmin)

admin.site.site_header = 'Affulence Market Reports'
admin.site.site_title = 'Admin | Affulence Market Reports'
admin.site.index_title = 'Admin | Affulence Market Reports'