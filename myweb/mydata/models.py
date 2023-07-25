from django.db import models

# Create your models here.
class contact(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.first_name
    