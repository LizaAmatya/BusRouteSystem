import django_tables2 as tables
from .models import Bus, BusRoute, Route


class BusTable(tables.Table):
    
    bus_number = tables.TemplateColumn("{{ record.number }}")
    number_of_routes_this_bus_runs_on = tables.TemplateColumn(
        '<a href="{% url "busroute:bus_routes_list" record.id %}">{{ record.get_number_of_routes }}</a>')
    
    class Meta:
        model = Bus
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", "bus_number")
       

class BusRoutesTable(tables.Table):
    
    route_name = tables.TemplateColumn("{{ record.route.name }}")
    route_number = tables.TemplateColumn("{{ record.route.number }}")
    
    class Meta:
        model = BusRoute
        template_name = "django_tables2/bootstrap.html"
        fields = ("route_name", "route_number", "from_time", "to_time")


class RouteTable(tables.Table):

    route_number = tables.TemplateColumn("{{ record.number }}")
    number_of_bus_running_on_this_route = tables.TemplateColumn(
        '<a href="{% url "busroute:route_buses_list" record.id %}">{{ record.get_number_of_buses }}</a>')

    class Meta:
        model = Route
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", "route_number")


class BusRunningOnRouteTable(tables.Table):

    bus_name = tables.TemplateColumn("{{ record.bus.name }}")
    bus_number = tables.TemplateColumn("{{ record.bus.number }}")

    class Meta:
        model = BusRoute
        template_name = "django_tables2/bootstrap.html"
        fields = ("bus_name", "bus_number", "from_time", "to_time")
