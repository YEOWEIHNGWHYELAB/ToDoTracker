# Serializer helps us translate json and python data types because front end application
# send json data type and receive json data types it also controls what we receive on
# front end applications and what we should send back to front end as we don't want to
# send all the field from db to user

from rest_framework import serializers
from tasks.models import Category, Task


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['created_by']


class TaskSerializer(serializers.ModelSerializer):
    # When we return the task to the user, we will populate these 2 fields based on the
    # category model so we can use these fields on the UI
    # These are referenced from the categories table
    category_name = serializers.CharField(
        read_only=True, source='category.name'
    )
    category_color = serializers.CharField(
        read_only=True, source='category.color'
    )

    class Meta:
        model = Task
        fields = '__all__' # display all model fields with ModelSerializer
        read_only_fields = ['created_by']


class DashboardTaskCompletionStatSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField() # additional fields to be added

    class Meta:
        model = Task
        fields = ('completed', 'count') # only select these fields to display


class DashboardTaskByCategorySerializer(serializers.ModelSerializer):
    count = serializers.IntegerField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'color', 'count')
