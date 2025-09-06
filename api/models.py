from django.contrib.auth.models import AbstractUser, Group
from django.conf import settings

from django.db import models
from .core.BaseModel import BaseModel

from api.api_models import (
    School,
    Institute,
    Program,
    System,
    User,
    UserSystems,
    Student,
    CollectionCategory,
    Fee,
    AttendanceEvent,
    AttendanceRecord,
    EventSetting,
    Payment,
    PaymentSubmission,
)
