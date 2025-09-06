from django.db import models
from api.core.BaseModel import BaseModel


class AttendanceEvent(BaseModel):
    class EventStatus(models.TextChoices):
        UPCOMING = "upcoming", "Upcoming"
        ONGOING = "ongoing", "Ongoing"
        COMPLETED = "completed", "Completed"
        CANCELLED = "cancelled", "Cancelled"

    event_name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    event_status = models.CharField(
        max_length=20, choices=EventStatus.choices, default=EventStatus.UPCOMING
    )

    class Meta:
        db_table = "attendance_events"

    def __str__(self):
        return f"{self.event_name} ({self.get_event_status_display()})"
