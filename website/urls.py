from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('application/',application, name='application'),
    path('career/', career, name='careers'),
    path('adminrec/', adminrec, name='adminrec'),
    path('apply/', apply, name='employee-create'),
]
