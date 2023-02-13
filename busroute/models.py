from django.db import models
from django.db.models import Count


class Bus(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    number = models.CharField(max_length=10,null=False, blank=False)
    
    @property
    def get_number_of_routes(self):
        number_of_routes = BusRoute.objects.filter(bus=self).count()
        
        return number_of_routes
    
    
    def __str__(self) -> str:
        return self.name
    

class Route(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    number = models.IntegerField(null=True, blank=False)

    def __str__(self) -> str:
        return self.name
    
    @property
    def get_number_of_buses(self):
        number_of_buses = BusRoute.objects.filter(route=self).count()
        
        return number_of_buses
    
class BusRoute(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    from_time = models.DateTimeField()
    to_time = models.DateTimeField()

