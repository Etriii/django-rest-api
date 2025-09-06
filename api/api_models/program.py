from django.db import models
from api.core.BaseModel import BaseModel


class Program(BaseModel):
    class ProgramStatus(models.TextChoices):
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"

    name = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20, choices=ProgramStatus.choices, default=ProgramStatus.ACTIVE
    )
    institute = models.ForeignKey(  
        "Institute", on_delete=models.CASCADE, related_name="programs"
    )
    
    class Meta:
        db_table = "programs"

    def __str__(self):
        return self.name