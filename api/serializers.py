from dataclasses import field
from .models import Assistants,UserLogs,Leave
from rest_framework import serializers
from django.contrib.auth.models import User,Group
from rest_auth.serializers import UserDetailsSerializer

class AssistantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Assistants
        fields='__all__'

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Group
        fields='__all__'
        
class LeaveSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%Y-%m-%d",read_only=True)
    user = serializers.StringRelatedField()
    class Meta:
        model=Leave
        fields='__all__'

class UserLogsSerializer(serializers.ModelSerializer):
    time_in = serializers.TimeField(format="%H:%M:%S",read_only=True)
    time_out = serializers.TimeField(format="%H:%M:%S",read_only=True)
    user = serializers.StringRelatedField()
    class Meta:
        model=UserLogs
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    logs = UserLogsSerializer(read_only=True,many=True)
    leave = LeaveSerializer(read_only=True,many=True)
    assistants = AssistantSerializer(read_only=True,many=True)
    client = AssistantSerializer(read_only=True,many=True)
    groups = GroupSerializer(read_only=True,many=True)
    used_leave = serializers.IntegerField()
    earned_leave = serializers.IntegerField()
    class Meta:
        model=User
        fields='__all__'

class CustomUserSerializer(UserDetailsSerializer):
    logs = UserLogsSerializer(read_only=True,many=True)
    groups = GroupSerializer(read_only=True,many=True)
    class Meta:
        model=User
        fields='__all__'