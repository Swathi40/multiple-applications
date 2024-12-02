from food.views import*
from django.urls import path
urlpatterns=[
    path('veg/',veg,name='veg'),
    path('Nonveg/',Nonveg,name='Nonveg')
]