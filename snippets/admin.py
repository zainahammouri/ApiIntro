from django.contrib import admin
from .models import  Employees,diabetes, clothes

# Register your models here.
admin.site.register(Employees)
admin.site.register(diabetes)
admin.site.register(clothes)
