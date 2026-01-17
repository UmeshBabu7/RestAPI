from django.contrib import admin
from .models import TestModel


# Register your models here.

class TestModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone_number', 'address']


admin.site.register(TestModel, TestModelAdmin)