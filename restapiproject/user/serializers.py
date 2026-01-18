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
    
    
    # username
    def validate_username(self, username1):
        if User.objects.filter(username=username1).exists():
            raise serializers.ValidationError("Username Already Exists..")
        
        return username1
    
    # password
    def validate_password(self, password1):
        if len(password1)<5:
            raise serializers.ValidationError("Password at least 6 characters...")
        
        return password1
    