from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import TestModel
from .serializers import TestModelSerializers
from restapi_app import global_message


# Create your views here.

class TestView(APIView):
    def get(self, request):
        try:
            test = TestModel.objects.all()
            serializer = TestModelSerializers(test, many=True) # queryset to native python data
            return Response({global_message.RESPONSE_MESSAGE:global_message.SUCCESS_MESSAGE, global_message.DATA:serializer.data}, status=status.HTTP_200_OK)
        
        except Exception as exe:
            print(exe)
            return Response({global_message.RESPONSE_MESSAGE:global_message.INTERNAL_ERROR})


    def post(self, request):
        try:
            serializer = TestModelSerializers(data= request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({global_message.RESPONSE_MESSAGE:global_message.DATA_CREATED}, status=status.HTTP_201_CREATED)
            
            return Response({global_message.RESPONSE_MESSAGE:serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as exe:
            print(exe)
            return Response({global_message.RESPONSE_MESSAGE:global_message.INTERNAL_ERROR}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


# update(put)
class TestViewUpdate(APIView):
    def put(self, request, id ):
        try:
            instance = TestModel.objects.get(id=id)
            serializer = TestModelSerializers(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({global_message.RESPONSE_MESSAGE:global_message.DATA_UPDATED}, status=status.HTTP_201_CREATED)
            
            return Response({global_message.RESPONSE_MESSAGE:serializer.erros}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as exe:
            print(exe)
            return Response({global_message.RESPONSE_MESSAGE:global_message.INTERNAL_ERROR}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class TestViewDelete(APIView):
    def delete(self, request, id):
        try:
            instance = TestModel.objects.get(id=id)
            instance.delete()

            return Response({global_message.RESPONSE_MESSAGE:global_message.DATA_DELETED}, status=status.HTTP_204_NO_CONTENT)
        
        except TestModel.DoesNotExist:
            return Response({global_message.RESPONSE_MESSAGE:global_message.DATA_ERROR}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as exe:
            print(exe)
            return Response({global_message.RESPONSE_MESSAGE:global_message.INTERNAL_ERROR}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
