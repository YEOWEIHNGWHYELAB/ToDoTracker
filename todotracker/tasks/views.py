from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from rest_framework.response import Response
from .serializers import CategorySerializer, TaskSerializer, DashboardTaskCompletionStatSerializer, DashboardTaskByCategorySerializer
from rest_framework.pagination import PageNumberPagination
from django.db.models import Count
from django.db.models.query_utils import Q
from .models import Category, Task
from .permissions import TaskPermission


# Create your views here.
class StandardResultSetPagination(PageNumberPagination):
    page_size = 6  # Default number of records per page when not specified
    page_size_query_param = 'page_size'
    max_page_size = 6  # Max Limit


# Using model view set to help us handle common operation such as
# creating a category, getting a list of category and getting a
# single category by id, updating a category, deleting category
class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = CategorySerializer

    # Return only the categories that belong to that current user
    def get_queryset(self):
        return self.request.user.categories.all()

    # When a category is created, we mark that with the user that created it
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
        TaskPermission
    ]
    serializer_class = TaskSerializer
    pagination_class = StandardResultSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title'] # Search by what
    ordering_fields = ['completed', '-created_at'] # order by
    ordering = ['completed', '-created_at']

    # Return all of the task that belong to the current authenticated user
    def get_queryset(self):
        # Check if the user included the query params in the url, and we update the
        # query param dictionary to include or provide the query params then pass it
        # to filter object
        user = self.request.user
        completed = self.request.query_params.get('completed')
        priority = self.request.query_params.get('priority')
        category = self.request.query_params.get('category')
        query_params = {}

        if completed is not None:
            query_params["completed"] = completed

        if priority is not None:
            query_params["priority"] = priority

        if category is not None:
            query_params["category"] = category

        return Task.objects.filter(created_by=user, **query_params)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user) # update the created_by field


class DashboardTaskCompletionStatViewSet(viewsets.ViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def list(self, request):
        user = self.request.user

        # show the task by that user based on completion and annotate with the count where its completed
        queryset = Task.objects.filter(created_by=user).values('completed').annotate(count=Count('completed'))
        serializer = DashboardTaskCompletionStatSerializer(queryset, many=True)
        return Response(serializer.data)


class DashboardTaskByCategoryViewSet(viewsets.ViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    # Indicates the number of objects inside a particular category
    def list(self, request):
        user = self.request.user
        tasks_filter = {}
        completed = self.request.query_params.get('completed')
        if completed is not None:
            tasks_filter['tasks__completed'] = completed
        queryset = Category.objects.filter(created_by=user).annotate(count=Count('tasks', filter=Q(**tasks_filter)))
        serializer = DashboardTaskByCategorySerializer(queryset, many=True)
        return Response(serializer.data)
