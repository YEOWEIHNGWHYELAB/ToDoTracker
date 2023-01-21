from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.db.models import Q
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


# CustomUserManager extends UserManager
class CustomUserManager(UserManager):
    # A Q() object represents an SQL condition that can be used in database-related operations.
    # Update get_by_natural_key method inherited from UserManager, it finds user by using email/username
    def get_by_natural_key(self, username):
        return self.get(Q(**{self.model.USERNAME_FIELD: username}) | Q(**{self.model.EMAIL_FIELD: username}))


# Create your models here, updated the CustomUser to use CustomUserManager instead of DefaultUserManager
# If you don’t specify primary_key=True for any fields in your model, Django will automatically add
# an IntegerField to hold the primary key
class CustomUser(AbstractUser):
    # Validate only alphanumeric characters and prints message if not fulfilled
    username_validator = RegexValidator(r'^[0-9a-zA-Z]*$', 'PLEASE ONLY ENTER ALPHANUMERIC CHARACTERS')
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "PLEASE ONLY ENTER ALPHANUMERIC CHARACTERS"
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    email = models.EmailField(blank=False, unique=True)  # Let user login using their email
    objects = CustomUserManager()
