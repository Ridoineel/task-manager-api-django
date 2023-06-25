from django.urls import path, include
from rest_framework import routers

from api_task.views import TaskViewSet

app_name = "api_task"

# router creation
router = routers.SimpleRouter()

router.register('', TaskViewSet, basename='task')

urlpatterns = [
	path("", include(router.urls))
]