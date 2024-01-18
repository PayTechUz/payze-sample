"""
the base database model.
"""
from django.db import models


class BaseModel(models.Model):
    """
    the base model class for users.
    """
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        the base model meta class fields.
        """
        abstract = True
