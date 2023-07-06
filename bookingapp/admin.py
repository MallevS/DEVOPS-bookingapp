from django.contrib import admin

# Register your models here.
from .models import *


class DepartmentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Department, DepartmentAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['user', 'department','room']
    pass


admin.site.register(Employee, EmployeeAdmin)


class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'capacity']
    pass


admin.site.register(Room, RoomAdmin)


class BookingAdmin(admin.ModelAdmin):
    list_display = ['room','start_time', 'end_time', 'employee_count']

    def employee_count(self, obj):
        return obj.user.count()

    employee_count.short_description = 'Employee Count'
    pass


admin.site.register(Booking, BookingAdmin)