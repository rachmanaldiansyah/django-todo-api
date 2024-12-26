from django.shortcuts import render

"""
TasksViewSet is a viewset for handling CRUD operations on Task objects.
Methods:
  create(request, *args, **kwargs):
    Handles the creation of a new Task object.
    - API Call: POST /api/tasks/
    - Request Body: JSON object with Task fields.
    - Response: 201 Created with the created Task object.
  update(request, *args, **kwargs):
    Handles the update of an existing Task object.
    - API Call: PUT /api/tasks/{id}/ or PATCH /api/tasks/{id}/
    - Request Body: JSON object with updated Task fields.
    - Response: 200 OK with the updated Task object.
  destroy(request, *args, **kwargs):
    Handles the deletion of an existing Task object.
    - API Call: DELETE /api/tasks/{id}/
    - Response: 204 No Content on successful deletion.
"""

from .models import Task
from .serializers import TaskSerializer

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

class TasksViewSet(viewsets.ModelViewSet):
  queryset = Task.objects.all()
  serializer_class = TaskSerializer
  # authentication_classes = [BasicAuthentication]
  # permission_classes = [IsAuthenticated]

  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    self.perform_create(serializer)
    headers = self.get_success_headers(serializer.data)
    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

  def update(self, request, *args, **kwargs):
    partial = kwargs.pop('partial', False)
    instance = self.get_object()
    serializer = self.get_serializer(instance, data=request.data, partial=partial)
    serializer.is_valid(raise_exception=True)
    self.perform_update(serializer)
    if getattr(instance, '_prefetched_objects_cache', None):
      instance._prefetched_objects_cache = {}
    return Response(serializer.data)

  def destroy(self, request, *args, **kwargs):
    instance = self.get_object()
    self.perform_destroy(instance)
    return Response(status=status.HTTP_204_NO_CONTENT)