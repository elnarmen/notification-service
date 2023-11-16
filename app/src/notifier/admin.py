from django.contrib import admin
from .models import Mailing, Client, Message


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'start_at', 'end_at', 'operator_code', 'client_tag']
    list_display_links = ['id', 'content']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone_number', 'operator_code', 'timezone', 'tag']
    list_display_links = ['id', 'phone_number']
    readonly_fields = ['operator_code']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'dispatch_at', 'status', 'mailing', 'client']
