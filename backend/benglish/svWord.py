from django.http.response import JsonResponse
from datetime import datetime
import pytz, json
from django.views.decorators.csrf import csrf_exempt
from backend.settings import sendResponse, connectDB, disconnectDB

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
        
        elif(action == 'select_word'): #echnee
            result = select_word(request)
            return (JsonResponse(result))
        elif(action == 'selectsub_word'): #echnee
            result = selectsub_word(request)
            return (JsonResponse(result))
        
        # elif(action == 'create_word'): #echnee
        #     result = create_word(request)
        #     return (JsonResponse(result))
        
        # elif(action == 'update_word'): #echnee
        #     result = word_update(request)
        #     return (JsonResponse(result))
        
        #  elif(action == 'word_delete'): #echnee
        #     result = word_delete(request)
        #     return (JsonResponse(result))
        else:
            action = action
            respData = []
            resp = sendResponse(action, 406, respData)
            return (JsonResponse(resp))
    elif request.method == "GET":
        return (JsonResponse({}))
    else :
        return (JsonResponse({}))

#{"action":"select_word" , "wid": 4}
def select_word(request):
    jsons = json.loads(request.body)
    action = jsons['action']
    try:
        wid=jsons['wid']
    except:
        action=action
        respData=[]
        resp=sendResponse(action, 10001, respData)
        return (resp)
    
    try:
        myConn = connectDB()
        cursor = myConn.cursor()
        query = f"""SELECT eng, mon, eng_sentence, translation, galig, zurag, wid, scid, created_at
	                FROM t_word  WHERE wid = {wid}"""
        cursor.execute(query)
        columns = cursor.description
        # print(columns)
        respRow = [{columns[index][0]:column for index , column in enumerate(value) } for value in cursor.fetchall()]
        
        # print(respRow)
    except:
        action=action
        respData=[]
        resp=sendResponse(action, 1001, respData)
        return (resp)
    finally: 
        cursor.close()
        disconnectDB(myConn)
    
    resp=sendResponse(action, 200, respRow)
    return resp 
# {"action":"selectsub_word" , "scid": 4}
def selectsub_word(request):
    jsons = json.loads(request.body)
    action = jsons['action']
    try:
        scid=jsons['scid']
    except:
        action=action
        respData=[]
        resp=sendResponse(action, 10001, respData)
        return (resp)
    
    try:
        myConn = connectDB()
        cursor = myConn.cursor()
        query = f"""SELECT eng, mon, eng_sentence, translation, galig, zurag, wid, scid, created_at
	                FROM t_word  WHERE scid = {scid}"""
        cursor.execute(query)
        columns = cursor.description
        # print(columns)
        respRow = [{columns[index][0]:column for index , column in enumerate(value) } for value in cursor.fetchall()]
        
        # print(respRow)
    except:
        action=action
        respData=[]
        resp=sendResponse(action, 1001, respData)
        return (resp)
    finally: 
        cursor.close()
        disconnectDB(myConn)
    
    resp=sendResponse(action, 200, respRow)
    return resp 



#{"action":"insert_word"}
def insert_word(request):
    jsons = json.loads(request.body)
    action = jsons['action']
    try:
        wid=jsons['wid']
    except:
        action=action
        respData=[]
        resp=sendResponse(action, 10001, respData)
        return (resp)
    
    try:
        myConn = connectDB()
        cursor = myConn.cursor()
        query = f"""SELECT eng, mon, eng_sentence, translation, galig, zurag, wid, scid, created_at
	                FROM t_word  WHERE wid = {wid}"""
        cursor.execute(query)
        columns = cursor.description
        # print(columns)
        respRow = [{columns[index][0]:column for index , column in enumerate(value) } for value in cursor.fetchall()]
        
        # print(respRow)
    except:
        action=action
        respData=[]
        resp=sendResponse(action, 1001, respData)
        return (resp)
    finally: 
        cursor.close()
        disconnectDB(myConn)
    
    resp=sendResponse(action, 200, respRow)
    return resp 

def update_word(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

    try:
        data = json.loads(request.body)
        action = data.get('action')
        wid = data.get('wid')

        if not wid:
            return sendResponse(action, 10001, [])

        fields = ['eng', 'mon', 'eng_sentence', 'translation', 'galig', 'zurag', 'scid']
        updates = {field: data.get(field) for field in fields if data.get(field) is not None}

        if not updates:
            return sendResponse(action, 10002, [])  # Nothing to update

        set_clause = ", ".join([f"{key} = %s" for key in updates])
        values = list(updates.values())

        values.append(wid)

        myConn = connectDB()
        cursor = myConn.cursor()
        query = f"UPDATE t_word SET {set_clause} WHERE wid = %s"
        cursor.execute(query, values)
        myConn.commit()

        return sendResponse(action, 200, {'updated': cursor.rowcount})

    except Exception as e:
        return sendResponse(action if 'action' in locals() else 'unknown', 1001, [])

    finally:
        try:
            cursor.close()
            disconnectDB(myConn)
        except:
            pass
        
def delete_word(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

    try:
        data = json.loads(request.body)
        action = data.get('action')
        wid = data.get('wid')

        if not wid:
            return sendResponse(action, 10001, [])

        myConn = connectDB()
        cursor = myConn.cursor()
        query = "DELETE FROM t_word WHERE wid = %s"
        cursor.execute(query, (wid,))
        myConn.commit()

        return sendResponse(action, 200, {'deleted': cursor.rowcount})

    except Exception as e:
        return sendResponse(action if 'action' in locals() else 'unknown', 1001, [])

    finally:
        try:
            cursor.close()
            disconnectDB(myConn)
        except:
            pass
#create
# def create_word(post):
#     jsons = jsons.loads(post.body)
#     action = jsons['action']
#     try:
#         uwid=json['uwid']
#     except:
#         action=action
#         respData=[]
#         resp=sendResponse(action, 1001, respData)
#         return (resp)
#     myConn=connectDB()
#     cursor=myConn.cursor()
#     query= f"INSERT uwid, uid, wid, regdata from t_word WHERE word = '{word}'"
#     cursor.execute(query)
#     columns=cursor.description
#     respRow = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
#     print(respRow)
    
#     finally: 
#         cursor.close()
#         disconnectDB(myConn)
    
#     resp=sendResponse(action, 2001, respRow)
#     return resp 

# #update
# def update_word(post):
#     jsons = jsons.loads(post.body)
#     action = jsons['action']
#     try:
#            uwid=json['uwid']
#     except:
#         action=action
#         respData=[]
#         resp=sendResponse(action, 1001, respData)
#         return (resp)
#     myConn=connectDB()
#     cursor=myConn.cursor()
#     query= f"UPDATE uwid, uid, wid, regdata from t_word WHERE word = '{word}'"
#     cursor.execute(query)
#     columns=cursor.description
#     respRow = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
#     print(respRow)
    
#     finally: 
#         cursor.close()
#         disconnectDB(myConn)
    
#     resp=sendResponse(action, 8001, respRow)
#     return resp 

# #delete
# def delete_word(post):
#     jsons = jsons.loads(post.body)
#     action = jsons['action']
#     try:
#         uwid=json['uwid']
#     except:
#         action=action
#         respData=[]
#         resp=sendResponse(action, 1001, respData)
#         return (resp)
#     myConn=connectDB()
#     cursor=myConn.cursor()
#     query= f"DELETE uwid, uid, wid, regdata from t_word WHERE word = '{word}'"
#     cursor.execute(query)
#     columns=cursor.description
#     respRow = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
#     print(respRow)
    
#     finally: 
#         cursor.close()
#         disconnectDB(myConn)
    
#     resp=sendResponse(action, 9001, respRow)
#     return resp 
    
    
