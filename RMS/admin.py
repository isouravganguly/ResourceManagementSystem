from django.contrib import admin

from .models import department, employees, products, transactions

# Register your models here.
admin.site.register(products)
admin.site.register(employees)
admin.site.register(transactions)
admin.site.register(department)