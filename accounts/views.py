from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupSerializer, ProfileSerializer
from .models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

# Create your views here.


# generics: CRUD 작업을 간단하게 처리하기 위한 기본적인 뷰 클래스 제공
class SignupView(generics.CreateAPIView):
    serializer_class = SignupSerializer


class ProfileView(generics.RetrieveAPIView):
    userse = User.objects.all()
    serializer_class = ProfileSerializer
    permission_class = [IsAuthenticated]

    def get_object(self):
        username = self.kwargs['username']
        user = User.objects.get(username=username)

        if self.request.user != user:
            raise PermissionDenied("너의 프로필이 아니야")

        return user
