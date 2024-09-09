from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupSerializer

# Create your views here.


# generics: CRUD 작업을 간단하게 처리하기 위한 기본적인 뷰 클래스 제공
class SignupView(generics.CreateAPIView):
    serializer_class = SignupSerializer
