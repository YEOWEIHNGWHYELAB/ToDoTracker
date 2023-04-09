from django.contrib import admin
from .models import Task, Category

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    # Header name, model's field to show
    list_display = ['title', 'created_at', 'completed', 'priority']


class CategoryAdmin(admin.ModelAdmin):
    # Header name, model's field to show
    list_display = ['name', 'color', 'created_at', 'created_by']


# Under the side panel, for tis particular tasks app, what
# will there be under tasks
admin.site.register(Task, TaskAdmin)
admin.site.register(Category, CategoryAdmin)
