from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from api_task.models import Task
from api_task.serializers import (
	TaskSerializer,
	TaskCreateSerializer,
	TaskListSerializer,
	TaskDetailSerializer,
	TaskUpdateSerializer
)
from api_task.views.base import BaseViewSet

class TaskViewSet(BaseViewSet, ModelViewSet):
	serializer_class = TaskListSerializer
	create_serializer_class = TaskCreateSerializer
	detail_serializer_class = TaskDetailSerializer
	update_serializer_class = TaskUpdateSerializer
	permission_classes =  [IsAuthenticated]

	def get_queryset(self):
		user = self.request.user

		queryset = Task.objects.filter(active=True, user=user)

		return queryset

	def perform_create(self, serializer):
		task = serializer.save(user=self.request.user)

		return task

	def perform_update(self, serializer):
		task = serializer.save(user=self.request.user)

		return task