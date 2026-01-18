from django.contrib.auth.models import User
from rest_framework import serializers



class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True) #create hudaina just read hunxa bahira dekhinxa
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True) # create hunxa tara tyo dekhdaina 


    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    