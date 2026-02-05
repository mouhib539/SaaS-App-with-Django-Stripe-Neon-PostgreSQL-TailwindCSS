from pathlib import Path
from django.db import models

BASE_DIR = Path(__file__).resolve().parent.parent

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    @staticmethod
    def get_vendor_path(filename: str) -> Path:
        """Returns the path where vendor files should be stored"""
        return BASE_DIR / "staticfiles" / "vendors" / filename
    
    def __str__(self):
        return self.name