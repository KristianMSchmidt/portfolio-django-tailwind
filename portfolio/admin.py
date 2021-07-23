from django.contrib import admin

# Register your models here.
from .models import Mail


class MailAdmin(admin.ModelAdmin):
    list_display = ('name', 'sender', 'subject', 'created_at', 'message')

admin.site.register(Mail, MailAdmin)
