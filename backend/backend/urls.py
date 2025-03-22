
from django.urls import path
from benglish import svTsag

urlpatterns = [
    path('tsag/', svTsag.dt_time), # localhost:8000/tsag/ gehed svTsag.dt_timecfunction duudna.
]
