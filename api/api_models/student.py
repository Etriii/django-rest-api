from django.db import models
from api.core.BaseModel import BaseModel

class Student(BaseModel):
    class StudentStatus(models.TextChoices):
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"
        GRADUATED = "graduated", "Graduated"
        DROPPED = "dropped", "Dropped"

    s_studentID = models.CharField(max_length=50, unique=True)
    program = models.ForeignKey(
        "Program", on_delete=models.CASCADE, related_name="students"
    )
    s_rfid = models.CharField(max_length=100, unique=True, null=True, blank=True)
    s_fname = models.CharField(max_length=100)
    s_mname = models.CharField(max_length=100, null=True, blank=True)
    s_lname = models.CharField(max_length=100)
    s_suffix = models.CharField(max_length=20, null=True, blank=True)
    s_email = models.EmailField(unique=True)
    s_set = models.CharField(max_length=50, null=True, blank=True)
    s_lvl = models.PositiveIntegerField()
    s_status = models.CharField(
        max_length=20, choices=StudentStatus.choices, default=StudentStatus.ACTIVE
    )
    s_image = models.ImageField(upload_to="students/", null=True, blank=True)
    
    class Meta:
        db_table = "students"

    def __str__(self):
        return f"{self.s_lname}, {self.s_fname} ({self.s_studentID})" 