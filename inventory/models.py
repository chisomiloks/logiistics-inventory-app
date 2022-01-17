from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from taggit.managers import TaggableManager


# Create your models here.
class Inventory(models.Model):
    title = models.CharField(max_length=50, default='')
    description = models.TextField()
    specifications = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    manufacturer = models.CharField(max_length=50, default='N/A')
    quantity = models.PositiveSmallIntegerField(default=0)
    tags = TaggableManager()
    merchant = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('inventory_detail', args=[str(self.id)])