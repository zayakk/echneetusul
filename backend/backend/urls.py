
from django.urls import path
from benglish import svTsag, svUser

urlpatterns = [
    path('tsag/', svTsag.checkService), # localhost:8000/tsag/ gehed svTsag.checkService function duudna.
    # path('tsagub/', svTsag.dt_timeub), # localhost:8000/tsag/ gehed svTsag.dt_time function duudna.
    path('user/', svUser.checkService),
]
