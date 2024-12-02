from ride.views import*
from django.urls import path
urlpatterns=[
    path('auto/',auto,name='auto'),
    path('bike/',bike,name='bike')

]