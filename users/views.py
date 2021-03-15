from rest_framework import viewsets
from rest_framework.response import Response
from .models import MyUser
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
from .serializers import MyUserSerializer
from django.core import serializers

class GetAllUsernames(viewsets.ModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer

