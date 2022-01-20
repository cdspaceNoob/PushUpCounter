from rest_framework import serializers
from .models import *


# model 직렬화
class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'
