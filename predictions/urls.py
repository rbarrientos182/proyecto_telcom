from django.urls import path
from .views import PredictChurnView #, CustomerListView # Asegúrate de que estos nombres existan en views.py

urlpatterns = [
    # Ruta para la predicción individual
    path('', PredictChurnView.as_view(), name='predict_churn'),
    
    # Ruta para el listado del Dashboard
    #path('list-all/', CustomerListView.as_view(), name='list_customers'),
]