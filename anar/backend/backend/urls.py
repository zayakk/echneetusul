
from django.urls import path
from benglish import svtsag
urlpatterns = [
    path('tsag/', svtsag.dt_time),
]
