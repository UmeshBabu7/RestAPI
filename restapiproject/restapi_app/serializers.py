from .models import TestModel
from rest_framework import serializers


class TestModelSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    phone_number = serializers.CharField(max_length=20)
    address = serializers.CharField(max_length=200)


    def create(self, validated_data):
        return TestModel.objects.create(**validated_data)
    

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance

