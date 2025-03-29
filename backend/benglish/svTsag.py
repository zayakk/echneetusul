from django.http.response import JsonResponse
from datetime import datetime
import pytz, json
from django.views.decorators.csrf import csrf_exempt
from backend.settings import sendResponse


def dt_time(request): #{key : value, key1 : value1, key2 : value2, }
    jsons = json.loads(request.body) # request.body-g dictionary boln avch baina
    action = jsons['action']
    respData = [{"tsag":str(datetime.now())}] # response-n data-g beldej baina. data key ni list baih buguud list dotor dictionary baina.
    resp = sendResponse(action, 200, respData)
    return (resp) # response bustsaaj baina

def dt_timeub(request): #{key : value, key1 : value1, key2 : value2, }
    jsons = json.loads(request.body) # request.body-g dictionary boln avch baina
    action = jsons['action']
    #Ulaanbaatar time zone
    ub_tz = pytz.timezone("Asia/Ulaanbaatar")
    
    #get current time in Ulaanbaatar
    ub_time = datetime.now(ub_tz)
    
    respData = [{"tsag":ub_time.strftime("%Y-%m-%d %H:%M:%S")}] # response-n data-g beldej baina. data key ni list baih buguud list dotor dictionary baina.
    resp = sendResponse(action, 200, respData)
    return (resp) # response bustsaaj baina

@csrf_exempt
def checkService(request): # hamgiin ehend duudagdah request shalgah function
    if request.method == "POST":
        try:
            jsons = json.loads(request.body) # request.body-g dictionary boln avch baina
        except: 
            action = "invalid request json"
            respData = []
            resp = sendResponse(action, 404, respData)
            return JsonResponse(resp)
        try:
            action = jsons["action"] # jsons-oos action key deh value-g action huvisagchid utga olgoj baina
        except:
            action = "no action key"
            respData = []
            resp = sendResponse(action, 404, respData)
            return JsonResponse(resp)
        
        if action == "tsag": # request.body -n action ni "tsag" baival ajillana.
            result = dt_time(request)
            return JsonResponse(result)
        elif action == "tsagub": # request.body -n action ni "tsagub" baival ajillana.
            result = dt_timeub(request)
            return JsonResponse(result)
        return (JsonResponse ({}))
    elif request.method == "GET":
        return (JsonResponse ({}))
