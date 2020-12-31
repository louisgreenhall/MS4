from django.db import models

# Create your models here.
class Invoice(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    invoice_number = models.TextField()
    request_id = models.IntegerField(default=0)
    amount = models.TextField()
    author = models.TextField()


