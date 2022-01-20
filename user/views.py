from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from .models import *
from .serializers import *



# 횟수, 시간 등의 정보를 보내준다
class Base(APIView):
    # For APP / username 또는 id에 의한 요청
    def get(self, request):
        data_get = JSONParser.parse(request)
        username_get = data_get['username']

        try:
            username = User.objects.filter(username=username_get)
        except User.DoesNotExist:
            return JsonResponse("Theres no username matched")

        if username_get == username:
            queryset = Data.objects.filter(username=username_get)
            serializer = DataSerializer(data=queryset)
            if serializer.is_valid():
                return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse("Not valid")



    # For HW / 기록 등록에 관한 요청
    def post(self, request):
        pass


# 앱 상에 그래프를 표시하기 위해 전달할 데이터
class Graph(APIView):
    def get(self, request):
        pass
