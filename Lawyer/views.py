from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Lawyer
from .serializers import UserSerializer

class UserCreateAPIView(generics.CreateAPIView):
    http_method_names = ['get','post']
    queryset = Lawyer.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)