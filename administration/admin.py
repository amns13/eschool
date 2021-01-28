from django.contrib import admin

from .models import Branch, Section, Student, Teacher


admin.site.register(Branch)
admin.site.register(Section)
admin.site.register(Student)
admin.site.register(Teacher)