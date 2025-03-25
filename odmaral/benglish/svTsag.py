from django.http.response import JsonResponse
from datetime import datetime

def dt_time(request):
    restData = [{"time":str(datetime.now())}]
    resp = {"action":"time", "data":restData, "size":1, 'resultCode':'200',
                          'resultMessage':'Success', "datetime":datetime.now()}
    return (JsonResponse(resp))