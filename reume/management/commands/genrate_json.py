from django.core.management.base import BaseCommand, CommandError

import json
import glob
from django.contrib.staticfiles.storage import staticfiles_storage


class Command(BaseCommand):

    def handle(self, *args, **options):
        pass


        data = """project_name
organization_name
date
what_did_you_do"""

        final_d = {}

        for i in data.split("\n"):

            final_d.update({i.strip():{
                'name': i.strip(),
                'placeholder': i.strip(),
                'label': i.strip(),

            }}
            )

        print(json.dumps(final_d,indent=3))