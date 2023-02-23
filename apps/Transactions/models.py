from apps.users.models import User
from django.db import models
from apps.categories.models import Category
from config.constants import *
from django.core.validators import MinValueValidator

# Create your models here.
class Transaction(models.Model):
    class Meta(object):
        db_table = 'transaction'

    name = models.CharField(
        'name', blank=False, null=False, max_length=200
    )

    user = models.ForeignKey(
       User, related_name='related_user', on_delete=models.CASCADE
    )

    category = models.ForeignKey(
        Category, related_name='related_category', on_delete=models.CASCADE
    )

    type = models.CharField(
        'Type', blank=False, null=False, max_length=50, choices=TRANSACTION_TYPE
    )

    amount = models.IntegerField(
        'amount', blank=False, null=False, validators=[
            MinValueValidator(1)
        ]
    )

    date = models.DateField(
        'date', blank=False, null=False
    )

    created_at = models.DateTimeField(
        'created_at', blank=True, null=False, auto_now_add=True
    )

    updated_at = models.DateTimeField(
        'Update Date', blank=True, auto_now_add=True
    )    
    def __str__(self):
        return self.name