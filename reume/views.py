import os

from django.http import HttpResponse
from django.shortcuts import render, redirect
import pdfkit
from django.template.loader import render_to_string
from django.urls import reverse
from django.contrib.staticfiles.storage import staticfiles_storage

from ResumeBuilder import settings
from reume.models import Resume, Contact, Socials, Experience, Education, Cources, Certicications, Objective, Project, \
    Skills


def home(request):
    return render(request, "xd_templates/Web_1920___1.html")


def download_pdf(request, resume_id):
    resume = Resume.objects.get(rid=resume_id)
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

    file_dir = os.path.join(settings.MEDIA_ROOT, 'pdfs/resume.pdf')

    pdfkit.from_string(render_to_string('reumes/onepageresume.html', context=context), file_dir)

    response = HttpResponse(open(file_dir, 'rb').read(), content_type="application/pdf")
    response['Content-Disposition'] = 'inline; filename=' + "resume.pdf"
    return response


def render_random_quiz(request, cat_id):
    return HttpResponse("You're looking at question %s." % cat_id)



def showresume(request,resume_id):

    return redirect('resume_about', resume_id)

def create_new_resume(request):
    resume = Resume()
    resume.save()

    return redirect('resume_about', resume_id=resume.rid)

def finalresume(request,resume_id):
    resume = Resume.objects.get(rid=resume_id)
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
    #html = render_to_string('reumes/onepageresume.html', context=context)

    context = {"resume_id": resume_id, "templ_type": "finalresume", "instance": None}
    return render(request, 'builder.html', context=context)

def show_resume(request, resume_id):
    resume = Resume.objects.get(rid=resume_id)
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
    return render(request, 'reumes/onepageresume.html', context=context)
