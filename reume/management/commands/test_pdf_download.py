import pdfkit
from django.core.management.base import BaseCommand, CommandError

import json
import glob
from django.contrib.staticfiles.storage import staticfiles_storage
from django.template.loader import render_to_string

from reume.models import Resume, Contact, Objective, Socials, Experience, Education, Skills, Project


class Command(BaseCommand):

    def handle(self, *args, **options):
        resume_id = 1
        resume = Resume.objects.get(id=resume_id)
        contact = Contact.objects.filter(resume=resume)
        objective = Objective.objects.filter(resume=resume)
        social = Socials.objects.filter(resume=resume)
        experience = Experience.objects.filter(resume=resume)
        education = Education.objects.filter(resume=resume)
        skill = Skills.objects.filter(resume=resume)
        project = Project.objects.filter(resume=resume)

        context = dict(
            contacts=contact,
            socials=social,
            experiences=experience,
            educations=education,
            skills=skill,
            projects=project,
            objectives=objective
        )
        pdfkit.from_string(render_to_string('reumes/onepageresume.html', context=context),'out.pdf')
