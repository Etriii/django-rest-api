from django.db import models
from api.core.BaseModel import BaseModel

class Institute(BaseModel):
    institute_name = models.CharField(max_length=255, unique=True)
    logo = models.TextField(max_length=1200)
    school = models.ForeignKey(  # ✅ replaced `school_id = CharField`
        "School", on_delete=models.CASCADE, related_name="institutes"
    )
    
    class Meta:
        db_table = "institutes"

    def __str__(self):
        return self.institute_name