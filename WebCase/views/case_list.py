# import json
# from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render

from WebCase.utils.form import *


def get_case_list(request):
    data_list = serializers.serialize("json", models.Case.objects.all())
    # data_list = models.Case.objects.all()
    # res_list = list(data_list)
    # for obj in data_list:
    #     print("模块", obj.get_caseChoices_display())
    res_list = {
        "msg": "success",
        "data": data_list
    }
    print(res_list)
    # return JsonResponse(res_list)
    return render(request, './caseList.html')
