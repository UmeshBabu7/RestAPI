from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import APIView
from rest_framework import status


# Create your views here.

class TestView(APIView):
    def get(self, request):
        return JsonResponse({"messages":"api testing..."}, status=200)


    def post(self, request):
        data = request.data 
        return JsonResponse({"messages":data}, status=200)
    