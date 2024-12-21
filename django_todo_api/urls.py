from django.contrib import admin
from django.urls import path, include

from api.tasks.views import TasksViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tasks', TasksViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
