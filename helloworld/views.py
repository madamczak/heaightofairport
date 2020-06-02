from django.shortcuts import render
from django.http import JsonResponse
import json


def main_view(request):
    return render(request, "main_view.html")


def get_all_icaos(request):
    # request_data = json.loads(request.body.decode('utf-8'))
    all_icaos= [{"icao": "KDEN", "height_before": 100, "height_after": 50, "diff": 50}]
    return JsonResponse({"all_icaos": all_icaos})

