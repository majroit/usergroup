from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .models import User, UserGroup
from .serializers import UserSerializer, UserGroupSerializer, UserGroupAddUserSerializer
from drf_yasg.utils import swagger_auto_schema

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserGroupViewSet(viewsets.ModelViewSet):
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer

    @swagger_auto_schema(
        request_body=UserGroupAddUserSerializer,
        responses={201: "User added", 400: "Invalid data", 404: "User not found"}
    )

    @action(detail=True, methods=['post'])
    def add_user(self, request, pk=None):
        group = self.get_object()
        serializer = UserGroupAddUserSerializer(data=request.data)  # Use the new serializer
        if serializer.is_valid():
            try:
                user = User.objects.get(pk=serializer.validated_data['user_id'])
                group.users.add(user)
                return Response({'status': 'user added'}, status=status.HTTP_201_CREATED)
            except User.DoesNotExist:
                return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=UserGroupAddUserSerializer,
        responses={204: "User removed", 400: "Invalid data", 404: "User not found"}
    )
    @action(detail=True, methods=['post'])
    def remove_user(self, request, pk=None):
        group = self.get_object()
        serializer = UserGroupAddUserSerializer(data=request.data)  # Use the new serializer
        if serializer.is_valid():
            try:
                user = User.objects.get(pk=serializer.validated_data['user_id'])
                group.users.remove(user)
                return Response({'status': 'user removed'}, status=status.HTTP_204_NO_CONTENT)
            except User.DoesNotExist:
                return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
