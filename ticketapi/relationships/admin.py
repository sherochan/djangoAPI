from django.contrib import admin

from .models import Student, Relationship
# Register your models here.
admin.site.register(Relationship)
admin.site.register(Student)
