from django.shortcuts import render
from rest_framework.views import APIView


# 횟수, 시간 등의 정보를 보내준다
class Base(APIView):
    # For APP / username 또는 id에 의한 요청
    def get(self, request):
        pass

    # For HW / 기록 등록에 관한 요청
    def post(self, request):
        pass


# 앱 상에 그래프를 표시하기 위해 전달할 데이터
class Graph(APIView):
    def get(self, request):
        pass
