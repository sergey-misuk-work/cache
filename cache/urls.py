from django.urls import path
from .views import daily, total

urlpatterns = [
    path('daily/', daily),
    path('total/', total),
]
