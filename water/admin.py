from django.contrib import admin
from .models import Order, Contact


class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'service', 'quantity')
    search_fields = ('name', 'mobile')
    list_filter = ('service',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'message')
    search_fields = ('name', 'mobile')


admin.site.register(Order, OrderAdmin)
admin.site.register(Contact, ContactAdmin)