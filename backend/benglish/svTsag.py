from django.http.response import JsonResponse
from datetime import datetime


def dt_time(request): #{key : value, key1 : value1, key2 : value2, }
    respData = [{"tsag":str(datetime.now())}]
    resp = {"action":"time","data":respData, "size":1,  "resultCode":"200", "resultMessage":"Success", "datetimes":datetime.now()}
    return (JsonResponse (resp))