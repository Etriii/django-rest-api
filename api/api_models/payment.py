from django.db import models
from api.core.BaseModel import BaseModel
from django.conf import settings


class Payment(BaseModel):
    class PaymentMethod(models.TextChoices):
        CASH = "cash", "Cash"
        GCASH = "gcash", "GCash"
        BANK = "bank", "Bank Transfer"
        ONLINE = "online", "Online Payment"
        OTHER = "other", "Other"

    fee = models.ForeignKey("Fee", on_delete=models.CASCADE, related_name="payments")
    amount_paid = models.DecimalField(max_digits=12, decimal_places=2)
    payment_method = models.CharField(
        max_length=20, choices=PaymentMethod.choices, default=PaymentMethod.CASH
    )
    received_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="received_payments",
    )
    payment_submission = models.ForeignKey(
        "PaymentSubmission",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="payments",
    )

    class Meta:
        db_table = "payments"
        # ordering = ["-created_at"]
        pass

    def __str__(self):
        return f"Payment {self.id} - {self.amount_paid} ({self.payment_method})"
