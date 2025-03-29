from django.http.response import JsonResponse
from datetime import datetime
import pytz, json
from django.views.decorators.csrf import csrf_exempt
from backend.settings import sendResponse,connectDB, disconnectDB


def dt_dropuserword(request):
    jsons = json.loads(request.body)
    action = jsons['action'] # commit
    try:
        uid = jsons['uid']
        wid = jsons['wid']
    except:
        action = action
        respData = []
        resp = sendResponse(action, 1005, respData) # 1005 zasah
        return (resp)
    
    myConn = connectDB()
    cursor = myConn.cursor()
    query = f"DELETE FROM t_userword WHERE uid = {uid} and wid = {wid}"
    cursor.execute(query)
    myConn.commit()
    
    query = f"SELECT * FROM t_word WHERE wid = {wid}"
    cursor.execute(query)
    columns = cursor.description
    # print(columns)
    respRow = [{columns[index][0]:column for index , column in enumerate(value) } for value in cursor.fetchall()]
    
    resp = sendResponse(action, 5003, respRow)
    
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
        if(action == 'dropuserword'):
            result = dt_dropuserword(request)
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