from django.db import models

# Create your models here.

class Category(models.Model):
    class Meta(object):
        db_table = 'category'
        verbose_name_plural = "Categories"

    name = models.CharField(
        'name', blank=False, null=False, max_length=200
    )

    color_code = models.CharField(
        'color_code', blank=False, null=False, max_length=50
    )

    created_at = models.DateTimeField(
        'created_at', blank=True, null=False, auto_now_add=True
    )

    updated_at = models.DateTimeField(
        'updated_at', blank=True, auto_now_add=True
    )    

    def __str__(self): 
        return self.name