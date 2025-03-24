from django.http.response import JsonResponse
from datetime import datetime
import pytz, json


def dt_time(request): #{key : value, key1 : value1, key2 : value2, }
    respData = [{"tsag":str(datetime.now())}] # response-n data-g beldej baina. data key ni list baih buguud list dotor dictionary baina.
    resp = {"action":"time","data":respData, "size":1,  "resultCode":"200", "resultMessage":"Success", "curdate":datetime.now()} # response beldej baina. 6 keytei
    return (resp) # response bustsaaj baina

def dt_timeub(request): #{key : value, key1 : value1, key2 : value2, }
    #Ulaanbaatar time zone
    ub_tz = pytz.timezone("Asia/Ulaanbaatar")
    
    #get current time in Ulaanbaatar
    ub_time = datetime.now(ub_tz)
    
    respData = [{"tsag":ub_time.strftime("%Y-%m-%d %H:%M:%S")}] # response-n data-g beldej baina. data key ni list baih buguud list dotor dictionary baina.
    resp = {"action":"time","data":respData, "size":1,  "resultCode":"200", "resultMessage":"Success", "curdate":datetime.now()} # response beldej baina. 6 keytei
    return (resp) # response bustsaaj baina


def checkService(request): # hamgiin ehend duudagdah request shalgah function
    jsons = json.loads(request.body) # request.body-g dictionary boln avch baina
    # print(jsons)
    action = jsons['action'] # jsons-oos action key deh value-g action huvisagchid utga olgoj baina
    # print(action)
    if action == "tsag": # request.body -n action ni "tsag" baival ajillana.
        result = dt_time(request)
        return JsonResponse(result)
    elif action == "tsagub": # request.body -n action ni "tsagub" baival ajillana.
        result = dt_timeub(request)
        return JsonResponse(result)
    return (JsonResponse ({}))