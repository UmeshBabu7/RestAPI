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
        


# update(put)
class TestViewUpdate(APIView):
    def put(self, request, id ):
        try:
            instance = TestModel.objects.get(id=id)
            serializer = TestModelSerializers(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data":"data successfully updated.."}, status=status.HTTP_201_CREATED)
            
            return Response({"data":serializer.erros}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as exe:
            print(exe)
            return Response({"messages":"Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class TestViewDelete(APIView):
    def delete(self, request, id):
        try:
            instance = TestModel.objects.get(id=id)
            instance.delete()

            return Response({"messages":"data successfully deleted.."}, status=status.HTTP_204_NO_CONTENT)
        
        except TestModel.DoesNotExist:
            return Response({"message":"Data not found.."}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as exe:
            print(exe)
            return Response({"message":"Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
