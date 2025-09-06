from django.db import models
from api.core.BaseModel import BaseModel
from django.conf import settings


class PaymentSubmission(BaseModel):
    class SubmissionStatus(models.TextChoices):
        PENDING = "pending", "Pending Review"
        APPROVED = "approved", "Approved"
        REJECTED = "rejected", "Rejected"

    student = models.ForeignKey(
        "Student", on_delete=models.CASCADE, related_name="payment_submissions"
    )
    fee = models.ForeignKey(
        "Fee", on_delete=models.CASCADE, related_name="payment_submissions"
    )
    screenshot = models.ImageField(
        upload_to="payment_screenshots/", null=True, blank=True
    )  # screenshot_path
    amount_paid = models.DecimalField(max_digits=12, decimal_places=2)
    reference_number = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=SubmissionStatus.choices,
        default=SubmissionStatus.PENDING,
    )
    reviewed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reviewed_submissions",
    )
    reviewed_at = models.DateTimeField(null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "payment_submissions"
        # ordering = ["-created_at"]
        pass

    def __str__(self):
        return f"Submission {self.id} - {self.student.student_id} ({self.status})"
