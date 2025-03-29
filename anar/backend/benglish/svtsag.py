from django.http.response import JsonResponse
from datetime import datetime

def dt_time(request):
    data=[{"time":datetime.now()}]
    return (JsonResponse({"action":"tsag", "data":data, "resultCode":200, "resultMessage":"Success", "size":len(data), "curdate":datetime.now()}))
    return(resp)


@csrf_exempt
def checkservice(request):
    if request.method == "POST":
        action = json.loads(request.body)
        print(jsons)
        result=dt_time(request)
        return (JsonResponse(result))
