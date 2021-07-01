from rest_framework import viewsets
from .models import MyUser
from rest_framework.renderers import JSONRenderer
from .serializers import MyUserSerializer
from rest_framework.permissions import IsAuthenticated

class GetAllUsernames(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = MyUser.objects.all()
        return queryset

    def get_serializer_class(self):
        serializer_class = MyUserSerializer
        return serializer_class

    renderer_classes = [JSONRenderer]



