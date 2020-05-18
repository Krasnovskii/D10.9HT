from django.db import models

class Car(models.Model):
    manufacturer = models.CharField(max_length=15)
    car_model = models.CharField(max_length=15)
    year_of_issue = models.IntegerField()
    # Выбор коробки автомобиля
    TRANSMISION_CHOICES = (
        ('Manual', 'Manual'),
        ('Automatic', 'Automatic' ),
        ('Robot', 'Robot'),
    )
    transmition = models.CharField(max_length=10, choices=TRANSMISION_CHOICES)
    # Выбор коробки автомобиля

    # Выбор цвета автомобиля
    COLOR_CHOICES = (
        ('Red', 'Red'),
        ('Green', 'Green'),
        ('Black', 'Black'),
        ('Withe', 'Withe'),
        ('Gray', 'Gray')
    )
    color = models.CharField(max_length=10, choices=COLOR_CHOICES)
    # Выбор цвета автомобиля
    #отобрадение списка автомобилей в адмике
    def __str__(self):
        template = '{0.manufacturer} {0.car_model} {0.color}'
        return template.format(self)
