from django.urls import path
from .views import EquationCreate

urlpatterns = [
    path('qcalculus', EquationCreate.as_view()),
]