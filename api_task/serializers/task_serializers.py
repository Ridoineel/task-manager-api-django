from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from api_task.models import Task

class TaskSerializer(ModelSerializer):
	class Meta:
		model = Task
		fields = ("id", "user", "label", "description", "status", "active", "created_at", "updated_at")

class TaskListSerializer(TaskSerializer):
	pass

class TaskDetailSerializer(TaskSerializer):
	pass

class TaskWriteSerializer(TaskSerializer):
	active = serializers.BooleanField(read_only=True)

	class Meta(TaskSerializer.Meta):
		extra_kwargs = {
			"user": {"read_only": True}
		}

class TaskCreateSerializer(TaskWriteSerializer):
	# status = serializers.CharField(read_only=True)
	pass

class TaskUpdateSerializer(TaskWriteSerializer):
	pass