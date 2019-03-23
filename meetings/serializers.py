from rest_framework import serializers
from meetings.models import Meeting
from django.contrib.auth.models import User
from rest_framework import status
class MeetingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    sinceWhen = serializers.DateTimeField()
    tilWhen = serializers.DateTimeField()

    def validate(self,data):
        if data['sinceWhen'] >= data['tilWhen']:
            raise serializers.ValidationError("tilWhen must occur after sinceWhen")

        else:
            queryset = Meeting.objects.all()
            if (self.instance):
                for obj in queryset:
                    if(obj.id == self.instance.id):
                        continue
                    elif (data['tilWhen'] > obj.sinceWhen and data['sinceWhen'] < obj.tilWhen):
                        raise serializers.ValidationError("already exist reservation")

            else:
                for obj in queryset:
                    if (data['tilWhen'] > obj.sinceWhen and data['sinceWhen'] < obj.tilWhen):
                        raise serializers.ValidationError("already exist reservation")

        return data
    class Meta:
        model = Meeting
        fields = ('id','created', 'sinceWhen','tilWhen','user')

class UserSerializer(serializers.ModelSerializer):
    meetings = serializers.PrimaryKeyRelatedField(many=True, queryset=Meeting.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username' ,'meetings')
