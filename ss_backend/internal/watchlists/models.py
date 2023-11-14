from django.db import models
from django.db.models import Q



## Lists Table
class WatchList(models.Model):
    list_name = models.CharField(max_length=50)
    is_public = models.BooleanField(default=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["list_name"], condition=Q(is_public=True), name="unique_public_list_name"),
        ]

