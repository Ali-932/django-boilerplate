import uuid

from django.conf import settings
from django.db import models
from django_currentuser.db.models import CurrentUserField


class AbstractBaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    created_by = CurrentUserField(on_delete=models.SET_NULL,
                                  null=True,
                                  related_name="%(class)s_created")
    updated_by = CurrentUserField(on_delete=models.SET_NULL,
                                  null=True,
                                  related_name="%(class)s_created"
                                  , on_update=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']
