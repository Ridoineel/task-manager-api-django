from django.contrib import admin

from api_task.models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
	list_display = ("id", "user", "label", "description", "status", "active", "created_at", "updated_at")