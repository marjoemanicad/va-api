from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
from .views import UserLogsDetailView

router = DefaultRouter()
router.register('logs', UserLogsDetailView)
urlpatterns = router.urls

urlpatterns = [
    path("userlist/", views.UserListView.as_view(), name=""),
    path("client/<int:pk>/", views.UserDetailView.as_view(), name=""),
    path("assistant/", views.AssistListView.as_view(), name=""),
    path("assistant/<int:pk>/", views.AssistDetailView.as_view(), name=""),
    path('', include(router.urls))

]
