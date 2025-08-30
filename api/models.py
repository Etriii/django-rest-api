from django.contrib.auth.models import (
    AbstractUser,
    Group,
)
from core.BaseModel import BaseModel
from django.db import models
from django.utils import timezone


class School(BaseModel):
    school_name = models.CharField(max_length=100, unique=True)
    logo = models.TextField(max_length=1200)
    location = models.TextField(max_length=1200)


class Institute(BaseModel):
    institute_name = models.CharField(max_length=255, unique=True)
    logo = models.TextField(max_length=1200)
    school_id = models.CharField(20, unique=True)

    def __str__(self):
        return self.institute_name


class System(BaseModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class UserStatus(models.TextChoices):
    ACTIVE = "active", "Active"
    INACTIVE = "inactive", "Inactive"
    SUSPENDED = "suspended", "Suspended"
    
class CustomUser(AbstractUser, BaseModel):
    institute_id = models.CharField(max_length=100, null=True, blank=True)
    
    
    
class GroupProfile(BaseModel):
    group = models.OneToOneField(Group, on_delete=models.CASCADE, related_name="profile")
    system_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.group.name} ({self.system_id})"
    
"""
USAGE EXAMPLE

# Create user
user = CustomUser.objects.create_user(username="alex", password="1234", institute_id="INST001")

# Create group and attach system_id
from django.contrib.auth.models import Group
g = Group.objects.create(name="Admins")
GroupProfile.objects.create(group=g, system_id="SYS001")

# Assign user to group
user.groups.add(g)

# Access values
print(user.institute_id)         # "INST001"
print(g.profile.system_id)       # "SYS001"

"""
