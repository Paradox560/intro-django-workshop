from django.db import models

# Create your models here.
class Review(models.Model):
    review_text = models.CharField(max_length=100, blank=True)
    reviewer = models.CharField(max_length=100, blank=True)
    review_email = models.CharField(max_length=100, blank=True)
    review_number = models.CharField(max_length=10, blank=True)
