from django.db import models

class Task(models.Model):
	class TaskStatus(models.Choices):
		TODO="TODO"
		IN_PROGRESS="IN_PROGRESS"
		ON_HOLD="ON_HOLD"
		DONE="DONE"

	user = models.ForeignKey("auth.User", on_delete=models.CASCADE)

	label = models.CharField(max_length=256)
	description = models.CharField(max_length=256)
	status = models.CharField(max_length=32, choices=TaskStatus.choices, default=TaskStatus.TODO)
	active = models.BooleanField(default=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"Label: {self.label}, User: {self.user}"