from rest_framework import serializers
from meetings.models import Meeting
from django.contrib.auth.models import User

class MeetingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Meeting
        fields = ('id','created', 'sinceWhen','tilWhen','user')

class UserSerializer(serializers.ModelSerializer):
    meetings = serializers.PrimaryKeyRelatedField(many=True, queryset=Meeting.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username' ,'meetings')
