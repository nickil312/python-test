from rest_framework import serializers
from .models import *


class EmailSerializer(serializers.Serializer):
    subject = serializers.CharField()
    content = serializers.CharField()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        # fields = ["name", "description", "price", "exist"]
