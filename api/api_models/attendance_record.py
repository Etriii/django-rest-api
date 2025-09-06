from django.db import models
from api.core.BaseModel import BaseModel


class AttendanceRecord(BaseModel):
    student = models.ForeignKey(
        "Student", on_delete=models.CASCADE, related_name="attendance_records"
    )
    attendance_event = models.ForeignKey(
        "AttendanceEvent", on_delete=models.CASCADE, related_name="attendance_records"
    )
    morning_check_in = models.DateTimeField(null=True, blank=True)
    morning_check_out = models.DateTimeField(null=True, blank=True)
    afternoon_check_in = models.DateTimeField(null=True, blank=True)
    afternoon_check_out = models.DateTimeField(null=True, blank=True)
    total_fines = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fee = models.ForeignKey(
        "Fee",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="attendance_records",
    )
    date = models.DateField()

    class Meta:
        db_table = "attendance_records"

    def __str__(self):
        return f"{self.student.s_studentID} - {self.date}"
