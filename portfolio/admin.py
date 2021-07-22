from django.contrib import admin

# Register your models here.
from .models import Mail


class MailAdmin(admin.ModelAdmin):
    list_display = ('name', 'sender', 'subject')

admin.site.register(Mail, MailAdmin)
