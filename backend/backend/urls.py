
from django.urls import path
from benglish import svTsag

urlpatterns = [
    path('tsag/', svTsag.dt_time),
]
