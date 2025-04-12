from abc import abstractmethod
from django.http.response import JsonResponse
from datetime import datetime
import pytz, json
from django.views.decorators.csrf import csrf_exempt
from backend.settings import sendResponse

def dt_time(request): #{key : value, key1 : value1, key2 : value2, }
    jsons = json.loads(request.body)
    action = jsons['action']
    respData = [{"tsag":datetime.now()}] # response-n data-g beldej baina. data key ni list baih buguud list dotor dictionary baina.
    resp = sendResponse(action, 200, respData)
    return (resp) # response bustsaaj baina

def dt_hello(request):
    jsons = json.loads(request.body)
    action = jsons['action']
    respData = [{"result":"Hello world"}]
    resp = sendResponse(action, 200, respData)
    return resp

def dt_class(request):
    jsons = json.loads(request.body)
    action = jsons['action']
    respData = [{"result":"ECHNEE"}]
    resp = sendResponse(action, 200, respData)
    return resp

@csrf_exempt
def checkService(request):
    if request.method == "POST":
        try:
            jsons = json.loads( request.body)
        except: 
            action = "invalid request json"
            respData = []
            resp = sendResponse(action, 404, respData)
            return (JsonResponse(resp))
        # print(jsons)
        try: 
            action = jsons['action']
        except:
            action = "no action"
            respData = []
            resp = sendResponse(action, 400, respData)
            return (JsonResponse(resp))
        
        # print(action)
        if(action == 'time'):
            result = dt_time(request)
            return (JsonResponse(result))
        elif(action == 'hello'): #hello world
            result = dt_hello(request)
            return (JsonResponse(result))
        elif(action == 'class'): #echnee
            result = dt_class(request)
            return (JsonResponse(result))
        else:
            action = action
            respData = []
            resp = sendResponse(action, 406, respData)
            return (JsonResponse(resp))
    elif request.method == "GET":
        return (JsonResponse({"method":"GET"}))
    else :
        return (JsonResponse({"method":"BUSAD"}))
