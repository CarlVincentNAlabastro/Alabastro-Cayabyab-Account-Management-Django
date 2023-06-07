from django.db import models

class Account(models.Model):
    ACCOUNT_TYPES = (
        ('social', 'Social'),
        ('school', 'School'),
        ('gaming', 'Gaming'),
    )

    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPES)
    description = models.TextField(blank=True)  # New field

    def __str__(self):
        return self.username
