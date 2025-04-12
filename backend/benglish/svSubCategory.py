from django.http.response import JsonResponse
# from benglish import svSubCategory
import json
from django.views.decorators.csrf import csrf_exempt
from backend.settings import sendResponse, connectDB, disconnectDB


# {"action":"getsubcategory","scid":4}
def dt_getsubcategory(request):
    jsons = json.loads(request.body)
    action = jsons['action']
    try:
        scid = jsons['scid']
    except:
        action = action
        respData = []
        resp = sendResponse(action, 7001, respData)
        return (resp)
    
    myConn = connectDB()
    cursor = myConn.cursor()
    query = f"SELECT scid, cid, subname_en, subname_mn, created_at FROM t_subcategory WHERE scid={scid}"
    cursor.execute(query)
    columns = cursor.description
    # print(columns)
    respRow = [{columns[index][0]:column for index , column in enumerate(value) } for value in cursor.fetchall()]
    # print(respRow)
    cursor.close()
    disconnectDB(myConn)
    
    resp = sendResponse(action, 7002, respRow)
    return resp
# {"action":"getAllsubcategory","cid":1}

def dt_getAllsubcategory(request):
    jsons = json.loads(request.body)
    action = jsons['action']
    try:
        cid = jsons['cid']
    except:
        action = action
        respData = []
        resp = sendResponse(action, 7003, respData)
        return (resp)
    
    myConn = connectDB()
    cursor = myConn.cursor()
    if cid==0:
        query = f"SELECT scid, cid, subname_en, subname_mn, created_at FROM t_subcategory"
    
    else:
        query = f"SELECT scid, cid, subname_en, subname_mn, created_at FROM t_subcategory WHERE cid={cid}"
    cursor.execute(query)
    columns = cursor.description
    # print(columns)
    respRow = [{columns[index][0]:column for index , column in enumerate(value) } for value in cursor.fetchall()]
    # print(respRow)
    cursor.close()
    disconnectDB(myConn)
    
    resp = sendResponse(action, 7004, respRow)
    return resp


# CHECK SERVICE
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
        

        if action == 'getsubcategory':
            result = dt_getsubcategory(request)
            return (JsonResponse(result))

        elif action == 'getAllsubcategory':
            result = dt_getAllsubcategory(request)
            return (JsonResponse(result))

    return JsonResponse(sendResponse("invalid_method", 405, []))
