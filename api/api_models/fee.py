from django.db import models
from api.core.BaseModel import BaseModel
from django.conf import settings


class Fee(BaseModel):
    class FeeStatus(models.TextChoices):
        PENDING = "pending", "Pending"
        PARTIAL = "partial", "Partial"
        PAID = "paid", "Paid"
        WAIVED = "waived", "Waived"
        OVERDUE = "overdue", "Overdue"

    class Semester(models.TextChoices):
        FIRST = "1st", "First Semester"
        SECOND = "2nd", "Second Semester"

    student = models.ForeignKey(
        "Student", on_delete=models.CASCADE, related_name="fees"
    )
    category = models.ForeignKey(
        "CollectionCategory", on_delete=models.CASCADE, related_name="fees"
    )
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(
        max_length=20, choices=FeeStatus.choices, default=FeeStatus.PENDING
    )
    due_date = models.DateTimeField()
    issued_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="issued_fees",
    )
    remarks = models.TextField(null=True, blank=True)
    academic_year = models.PositiveIntegerField()
    semester = models.CharField(
        max_length=10, choices=Semester.choices, default=Semester.FIRST
    )

    class Meta:
        db_table = "fees"
        indexes = [
            models.Index(fields=["student", "academic_year", "semester"]),
        ]

    def __str__(self):
        return f"{self.student.s_studentID} - {self.category.category_name} ({self.status})"
