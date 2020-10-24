from django.http import HttpResponse
import json


def users(request):
    user_list=['alex','oldboy']
    return HttpResponse(json.dumps((user_list)))