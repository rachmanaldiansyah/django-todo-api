from django.db import models

class Task(models.Model):
  TODO = 'todo'
  DONE = 'done'

  STATUS_CHOICES = [
    (TODO, 'To Do'),
    (DONE, 'Done'),
  ]

  title = models.CharField(max_length=255)
  description = models.TextField()
  status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=TODO)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)