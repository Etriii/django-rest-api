from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from api.core.BaseModel import BaseModel


class User(AbstractUser, BaseModel):
    class UserStatus(models.TextChoices):
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"
        SUSPENDED = "suspended", "Suspended"

    status = models.CharField(
        max_length=20, choices=UserStatus.choices, default=UserStatus.ACTIVE
    )
    institute = models.ForeignKey(  # ✅ Proper FK instead of CharField
        "Institute",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="users",
    )
    
    class Meta:
        db_table = "users"

    def __str__(self):
        return self.username