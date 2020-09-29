from django.contrib import admin
from .models import Log, People, Aircraft, Airport
# Register your models here.


class LogAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'departure', 'arrival')


admin.site.register(Log, LogAdmin)
admin.site.register(People)
admin.site.register(Airport)
admin.site.register(Aircraft)