from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.

# Category Table/Model
class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return str(self.name) + " : " + str(self.created_by)

    # Attributes with constraints
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="categories", on_delete=models.CASCADE)


# Task Table/Model
class Task(models.Model):
    class Priority(models.IntegerChoices):
        # Tuples
        LOW = 1, "LOW"
        MEDIUM = 2, "MEDIUM"
        HIGH = 3, "HIGH"
        CRITICAL = 4, "CRITICAL"

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    priority = models.PositiveSmallIntegerField(choices=Priority.choices, default=Priority.MEDIUM)

    # Use models.ForeignKey for referencing the respective primary key which is
    # just an integer id when not specified in the referenced table
    category = models.ForeignKey(Category, related_name="tasks", on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name="tasks", on_delete=models.CASCADE)
