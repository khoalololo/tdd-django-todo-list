# lists/models.py
from django.db import models

class List(models.Model):
    # This model might be empty for now, or have a name field later
    pass # Or other fields like 'name = models.CharField(max_length=200)'

class Item(models.Model):
    text = models.TextField(default="")
    # --- ADD THIS LINE ---
    list = models.ForeignKey(List, default=None, on_delete=models.CASCADE)
    # --- END ADDITION ---

    def __str__(self):
        # Good practice: add a __str__ method for better representation in admin/shell
        return self.text