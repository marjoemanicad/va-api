from django.shortcuts import render
from requests import Response
from .models import Assistants,User,UserLogs
# Create your views here.
from .serializers import AssistantSerializer, CustomUserSerializer,UserSerializer,UserLogsSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthor
from rest_framework import viewsets
from datetime import datetime  
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count,Sum,OuterRef,Subquery
from pg_utils import DistinctSum
from rest_auth.views import UserDetailsView

class UserLogsDetailView(viewsets.ModelViewSet):
    queryset= UserLogs.objects.all()
    serializer_class = UserLogsSerializer
    permission_classes = [IsAuthenticated, IsAuthor]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        obj = self.get_object()
    
        a = obj.time_in.hour
        b = datetime.now().hour
        c = (b - a)
        d = (c * 0.0384)
        serializer.save(work_hours = c,earned_credit = d)

class UserListView(generics.ListAPIView):
    queryset= User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    firsta = User.objects.annotate(firstb=Sum('logs__work_hours')).filter(pk=OuterRef('pk'))
    second = User.objects.annotate(second=Sum('leave__used_hour')).filter(pk=OuterRef('pk'))
    queryset= User.objects.annotate(
        used_leave=Subquery(firsta.values('firstb')),
        earned_leave=Subquery(second.values('second'))
        )
    serializer_class = UserSerializer



class AssistListView(generics.ListAPIView):
    queryset= Assistants.objects.all()
    serializer_class = AssistantSerializer

class AssistDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Assistants.objects.all()
    serializer_class = AssistantSerializer