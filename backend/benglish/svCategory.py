from django.http.response import JsonResponse
from datetime import datetime
import pytz, json
from django.views.decorators.csrf import csrf_exempt
from backend.settings import sendResponse,connectDB, disconnectDB

def dt_time(request): #{key : value, key1 : value1, key2 : value2, }
    jsons = json.loads(request.body)
    action = jsons['action']
    respData = [{"tsag":str(datetime.now())}] # response-n data-g beldej baina. data key ni list baih buguud list dotor dictionary baina.
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

# {"action": "getCategory","cid":1}

def dt_getCategory(request):
    jsons = json.loads(request.body)
    action = jsons['action']
    try:
        cid = jsons['cid']
    except:
        action = action
        respData = []
        resp = sendResponse(action, 6001, respData)
        return (resp)
    myConn = connectDB()
    cursor = myConn.cursor()
    query = f"""SELECT cid, catname_en, catname_mn, created_at 
                FROM public.t_category
                where cid = {cid}"""
    cursor.execute(query)
    columns = cursor.description
    # print(columns)
    respRow = [{columns[index][0]:column for index , column in enumerate(value) } for value in cursor.fetchall()]
    # print(respRow)
    cursor.close()
    disconnectDB(myConn)
    
    resp = sendResponse(action, 6002, respRow)
    return resp

# {"action": "getAllCategory"}

def dt_getAllCategory(request):
    jsons = json.loads(request.body)
    action = jsons['action']
    # try:
    #     cid = jsons['cid']
    # except:
    #     action = action
    #     respData = []
    #     resp = sendResponse(action, 6001, respData)
    #     return (resp)
    myConn = connectDB()
    cursor = myConn.cursor()
    query = f"""SELECT cid, catname_en, catname_mn, created_at 
                FROM public.t_category
                """
    cursor.execute(query)
    columns = cursor.description
    # print(columns)
    respRow = [{columns[index][0]:column for index , column in enumerate(value) } for value in cursor.fetchall()]
    # print(respRow)
    cursor.close()
    disconnectDB(myConn)
    
    resp = sendResponse(action, 6003, respRow)
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
        
        elif(action == 'getCategory'): #echnee
            result = dt_getCategory(request)
            return (JsonResponse(result))
        
        elif(action == 'getAllCategory'): #echnee
            result = dt_getAllCategory(request)
            return (JsonResponse(result))
        else:
            action = action
            respData = []
            resp = sendResponse(action, 406, respData)
            return (JsonResponse(resp))
    elif request.method == "GET":
        return (JsonResponse({}))
    else :
        return (JsonResponse({}))
