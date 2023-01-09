import json
from django.http import JsonResponse
from django.core import serializers
from WebCase.utils.form import *


def get_case_list(request):
    data_list = serializers.serialize("json", models.Case.objects.all())
    print(data_list)
    return JsonResponse(data_list, safe=False)
