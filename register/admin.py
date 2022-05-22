from django.contrib import admin

from .models import Path, Student

admin.site.register(Student)
admin.site.register(Path)