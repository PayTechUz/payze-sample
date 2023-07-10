from django.db import models


class PaymentID(models.Model):
    """
    This model using for activating and validating the VISA cards.
    """
    PID = models.CharField(max_length=255, null=False, blank=False, unique=True)

    def __str__(self):
        return f"PID — {self.PID}"
