import helpers

from typing import Any

from django.core.management.base import BaseCommand
from django.conf import settings    
from commando.models import Vendor

STATICFILES_VENDORS_DIR = getattr(settings, "STATICFILES_VENDORS_DIR") 

VENDOR_STATICFILES = {
    "flowbite.min.js": "https://cdn.jsdelivr.net/npm/flowbite@4.0.1/dist/flowbite.min.js",
    "flowbite.min.css": "https://cdn.jsdelivr.net/npm/flowbite@4.0.1/dist/flowbite.min.css", 

}


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any):
        self.stdout.write("Pulling vendor files...")
        for name, url in VENDOR_STATICFILES.items():
            out_path = Vendor.get_vendor_path(name)
            helpers.download_to_local(url, out_path)
            self.stdout.write(f"Pulled {name} from {url} to {out_path}")