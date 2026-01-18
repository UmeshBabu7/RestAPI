from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.serializers import UserSerializer
from user import global_message



# register
class UserRegisterView(APIView):
    def get(self, request):
        try:
            user = User.objects.all()
            serializer = UserSerializer(user, many=True)
            return Response({global_message.RESPONSE_KEY:global_message.SUCCESS_MESSAGE, global_message.DATA:serializer.data}, status=status.HTTP_200_OK)
        
        except Exception as exe:
            print(exe)
        return Response({global_message.RESPONSE_KEY:global_message.INTERNAL_MESSAGE}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = UserSerializer(data= request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({global_message.RESPONSE_KEY:global_message.USER_CREATE}, status=status.HTTP_200_OK)
            
            return Response({global_message.RESPONSE_KEY:serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as exe:
            print(exe)
            return Response({global_message.RESPONSE_KEY:global_message.INTERNAL_MESSAGE}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
