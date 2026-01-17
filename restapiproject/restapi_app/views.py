from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import TestModel
from .serializers import TestModelSerializers


# Create your views here.

class TestView(APIView):
    def get(self, request):
        try:
            data = TestModel.objects.all()
            serializer = TestModelSerializers(data, many=True) # queryset to native python data
            return Response({"data":serializer.data}, status=status.HTTP_200_OK)
        
        except Exception as exe:
            print(exe)
            return Response({"messages":"Internal server error"})


    def post(self, request):
        try:
            serializer = TestModelSerializers(data= request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"messages":"data successfully saved.."}, status=status.HTTP_201_CREATED)
            
            return Response({"messages":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as exe:
            print(exe)
            return Response({"messages":"Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    