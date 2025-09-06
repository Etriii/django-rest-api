from django.db import models
from api.core.BaseModel import BaseModel


class EventSetting(BaseModel):
    class EventStatus(models.TextChoices):
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"
        CLOSED = "closed", "Closed"

    attendance_event = models.ForeignKey(
        "AttendanceEvent", on_delete=models.CASCADE, related_name="settings"
    )
    date = models.DateField()

    # Morning session
    checkin_start = models.DateTimeField()
    checkin_end = models.DateTimeField()
    checkout_start = models.DateTimeField()
    checkout_end = models.DateTimeField()

    # Afternoon session
    afternoon_checkin_start = models.DateTimeField(null=True, blank=True)
    afternoon_checkin_end = models.DateTimeField(null=True, blank=True)
    afternoon_checkout_start = models.DateTimeField(null=True, blank=True)
    afternoon_checkout_end = models.DateTimeField(null=True, blank=True)

    event_status = models.CharField(
        max_length=20, choices=EventStatus.choices, default=EventStatus.ACTIVE
    )

    class Meta:
        db_table = "event_settings"
        # ordering = ["date"]
        # unique_together = ("attendance_event", "date")  # avoid duplicate settings for same event/date
        pass

    def __str__(self):
        return f"{self.attendance_event.event_name} - {self.date}"
