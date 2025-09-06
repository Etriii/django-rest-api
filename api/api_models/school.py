from django.db import models
from api.core.BaseModel import BaseModel

class School(BaseModel):
    school_name = models.CharField(max_length=100, unique=True)
    logo = models.TextField(max_length=1200)
    location = models.TextField(max_length=1200)

    class Meta:
        db_table = "schools"

    def __str__(self):
        return self.school_name
