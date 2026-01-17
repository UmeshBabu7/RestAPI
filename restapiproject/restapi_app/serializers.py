from .models import TestModel
from rest_framework import serializers


class TestModelSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    phone_number = serializers.CharField(max_length=20)
    address = serializers.CharField(max_length=200)


    def create(self, validated_data):
        return TestModel.objects.create(**validated_data)

