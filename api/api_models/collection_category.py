from django.db import models
from api.core.BaseModel import BaseModel


class CollectionCategory(BaseModel):
    category_name = models.CharField(max_length=150)
    collection_fee = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    institute = models.ForeignKey(
        "Institute", on_delete=models.CASCADE, related_name="collection_categories"
    )

    class Meta:
        db_table = "collection_categories"
        # ordering = ["category_name"]
        # unique_together = ("category_name", "institute")
        pass

    def __str__(self):
        return f"{self.category_name} ({self.collection_fee})"
