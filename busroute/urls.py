from django.urls import path
from django.conf.urls import include

from busroute.views import BusListView, BusRoutesViewList, BusesRunningOnARouteViewList, RouteListView, home

app_name = "busroute"

urlpatterns = [
    path('',home, name='index'),
    path('buses/', BusListView.as_view(), name='bus_list'),
    path('bus/routes/<int:pk>', BusRoutesViewList.as_view(), name="bus_routes_list"),
    path('routes/', RouteListView.as_view(), name='route_list'),
    path('route/buses<int:pk>', BusesRunningOnARouteViewList.as_view(), name="route_buses_list"),

]
