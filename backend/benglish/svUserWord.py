from django.http.response import JsonResponse
from datetime import datetime
import pytz, json
from django.views.decorators.csrf import csrf_exempt
from backend.settings import sendResponse,connectDB, disconnectDB

def dt_addedword(request):
    jsons = json.loads(request.body)
    action = jsons['action']
    try:
        uid = jsons['uid']
        wid = jsons['wid']
    except:
        action = action
        respData = []
        resp = sendResponse(action, 1002, respData)
        return (resp)
    
    myConn = connectDB()
    cursor = myConn.cursor()

    query = f"INSERT INTO t_userword(uid, wid) VALUES({uid},{wid})"
    cursor.execute(query)
    myConn.commit()

    query = f"SELECT * FROM t_word WHERE wid = {wid}"
    cursor.execute(query)
    columns = cursor.description
    # print(columns)
    respRow = [{columns[index][0]:column for index , column in enumerate(value) } for value in cursor.fetchall()]
    
    resp = sendResponse(action, 1003, respRow)

    return resp

# {"action":"getUserWord","uid":1}
def dt_getUserWord(request):


    jsons = json.loads(request.body)
    action = jsons['action']
    try:
        uid = jsons['uid']
        # wid = jsons['wid']
    except:
        action = action
        respData = []
        resp = sendResponse(action, 4001, respData)
        return (resp)

    myConn = connectDB()
    cursor = myConn.cursor()

    query = f"SELECT * FROM t_userword WHERE uid = {uid} order by wid asc"
    cursor.execute(query)
    columns = cursor.description
    # print(columns)
    respData = [{columns[index][0]:column for index , column in enumerate(value) } for value in cursor.fetchall()]
    
    resp = sendResponse(action, 4002, respData)

    return resp


def dt_DeleteUserWord(request):
    jsons = json.loads(request.body)
    action = jsons['action']
    try:
        uid = jsons['uid']
        wid = jsons['wid']
    except:
        action = action
        respData = []
        resp = sendResponse(action, 4003, respData)
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
    respData = [{columns[index][0]:column for index , column in enumerate(value) } for value in cursor.fetchall()]
    
    resp = sendResponse(action, 4004, respData)

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
        if(action == 'UserWordadd'):
            result = dt_addedword(request)
            return (JsonResponse(result))
        elif(action == 'getUserWord'):
            result = dt_getUserWord(request)
            return (JsonResponse(result))
        elif(action == 'DeleteUserWord'):
            result = dt_DeleteUserWord(request)
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
    