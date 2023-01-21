from rest_framework import routers
from .views import CategoryViewSet, TaskViewSet, DashboardTaskCompletionStatViewSet, DashboardTaskByCategoryViewSet

# This is specific to DRF
# Generate the routing rules for category api to link to certain viewset
# r'' -> raw string
router = routers.DefaultRouter()
router.register(r'api/categories', CategoryViewSet, 'categories')
router.register(r'api/tasks', TaskViewSet, 'tasks')
router.register('api/dashboard/tasks-completion', DashboardTaskCompletionStatViewSet, 'tasks-completion')
router.register('api/dashboard/tasks-category-distribution', DashboardTaskByCategoryViewSet, 'tasks-category-distribution')

urlpatterns = router.urls
