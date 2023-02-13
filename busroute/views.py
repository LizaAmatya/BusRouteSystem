from django.shortcuts import redirect, render
# Create your views here.
from django.views.generic import DetailView, ListView
from django_tables2 import SingleTableView

from .models import Bus, BusRoute, Route
from .tables import BusRoutesTable, BusRunningOnRouteTable, BusTable, RouteTable


def home(request):
    return render(request, 'index.html')

class BusListView(SingleTableView):
    model = Bus
    table_class = BusTable
    template_name = 'bus/bus_list.html'


class BusRoutesViewList(DetailView):
    model = Bus
    template_name = 'bus/bus_routes_list.html'
    
    def get_context_data(self, **kwargs):
        table = BusRoutesTable(BusRoute.objects.filter(bus=self.object.pk))
        context = {"table": table}
        return super().get_context_data(**context)


class RouteListView(SingleTableView):
    model = Route
    table_class = RouteTable
    template_name = 'route/route_list.html'


class BusesRunningOnARouteViewList(DetailView):
    model = Route
    template_name = 'route/route_bus_list.html'

    def get_context_data(self, **kwargs):
        table = BusRunningOnRouteTable(
            BusRoute.objects.filter(route=self.object.pk))
        context = {"table": table}
        return super().get_context_data(**context)
