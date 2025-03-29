from django.http.response import JsonResponse
from datetime import datetime
import pytz, json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def dt_time(request):
    restData = [{"time":str(datetime.now())}]
    resp = {"action":"time", "data":restData, "size":1, 'resultCode':'200',
                          'resultMessage':'Success', "datetime":datetime.now()}
    return (resp)

@csrf_exempt
def dt_time_ub(request):
    ub_tz=pytz.timezone("Asia/Ulaanbaatar")

    ub_time = datetime.now(ub_tz)
    restData = [{"time":ub_time.strftime("%Y-%m-%d %H:%M:%S")}]
    resp = {"action":"time", "data":restData, "size":1, 'resultCode':'200',
                          'resultMessage':'Success', "datetime":datetime.now()}
    return (resp)

@csrf_exempt
def checkService(request):
    jsons = json.loads(request.body)
    action = jsons ['action']
    if action == "time":
        result = dt_time(request)
        return JsonResponse(result)
    elif action == "time_ub":
        result = dt_time_ub(request)
        return JsonResponse(result)
    return(JsonResponse({}))
