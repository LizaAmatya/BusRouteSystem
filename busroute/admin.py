from django.contrib import admin

from busroute.models import Bus, Route, BusRoute

# Register your models here.
admin.site.register([Bus, Route])

class BusRouteAdmin(admin.ModelAdmin):
    list_display = ['bus', 'route', 'from_time', 'to_time']

admin.site.register(BusRoute, BusRouteAdmin)
