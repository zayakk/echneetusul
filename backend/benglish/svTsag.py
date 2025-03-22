from django.http.response import JsonResponse
from datetime import datetime


def dt_time(request): #{key : value, key1 : value1, key2 : value2, }
    respData = [{"tsag":str(datetime.now())}] # response-n data-g beldej baina. data key ni list baih buguud list dotor dictionary baina.
    resp = {"action":"time","data":respData, "size":1,  "resultCode":"200", "resultMessage":"Success", "curdate":datetime.now()} # response beldej baina. 6 keytei
    return (JsonResponse (resp)) # response bustsaaj baina