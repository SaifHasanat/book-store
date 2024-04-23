from django.db import models
import uuid


class MyTransaction(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"amount:{self.amount}__currency:{self.currency}__id:{self.id},"
