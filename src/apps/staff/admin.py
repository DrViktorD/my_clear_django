from django.contrib import admin

from apps.staff.models import Position

class PositionAdmin(admin.ModelAdmin):
    list_display = ('short_name',)
    ordering = ['short_name']
admin.site.register(Position, PositionAdmin)
