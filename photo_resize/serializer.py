from .models import Photo
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ("photo", "width", "height")
    
    def validate(self, data):
        if data["width"] > 10000 or data["width"] <= 0 or data["height"] > 10000 or data["height"] <= 0:
            raise serializers.ValidationError({"message": "Размеры изображения должны иметь диапазон 1-10000"})
        return data

    def create(self, validated_data):
        return Photo.objects.create(**validated_data)
