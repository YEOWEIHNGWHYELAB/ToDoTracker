from rest_framework import permissions
from tasks.models import Category


class TaskPermission(permissions.BasePermission):
    message = 'Category not found!'

    def has_permission(self, request, view):
        # For create, update permission check...
        if view.action == 'create' or view.action == 'update' or view.action == 'partial_update':
            category = request.data.get('category')

            # If there is no category stated, user does not update the category
            if category is None:
                return True

            # Check the category that is to be modified, who is the request user?
            # And look up the database for that user.
            # This is basically a list of categories belonging to that user
            user_categories = Category.objects.filter(created_by=request.user).values_list('id', flat=True)

            # If the category provided does not exist in the current authenticated user,
            # we return false
            if not category in user_categories:
                return False

        # Otherwise return true
        return True
