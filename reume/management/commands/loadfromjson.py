from django.core.management.base import BaseCommand, CommandError

import json
import glob
from django.contrib.staticfiles.storage import staticfiles_storage


class Command(BaseCommand):

    def handle(self, *args, **options):
        pass
