from django.db.models.query_utils import Q
from .models import Car
from django.views.generic import ListView

#функция get запроса
class CarFilter:

    def get_car(self):
        return Car.objects.all()

#класс списка автомобилей
class CarList(CarFilter, ListView):
    model = Car
    template_name = 'car/car_list.html'

#класс фильтрайии
class FilterCarView(CarList, ListView):

    def get_queryset(self):
        queryset = Car.objects.filter(
            Q(manufacturer__in=self.request.GET.getlist('manufacturer')) |
            Q(transmition__in=self.request.GET.getlist('transmition'))
        )
        return queryset