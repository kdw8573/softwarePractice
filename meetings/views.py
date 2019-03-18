from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.response import Response
from meetings.models import Meeting
from meetings.serializers import MeetingSerializer
from meetings.serializers import UserSerializer
from meetings.permissions import OnlyUserCanAccess

class MeetingList(generics.ListCreateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class MeetingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, OnlyUserCanAccess)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
