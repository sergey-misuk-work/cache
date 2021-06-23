from django.urls import path
from .views import daily

urlpatterns = [
    path('daily/', daily),
]
