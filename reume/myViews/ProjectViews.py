from django.shortcuts import redirect, render

from reume.meta import meta_data_projects
from reume.models import Resume, Project


def projects(request, resume_id):
    resume = Resume.objects.get(id=resume_id)
    instances = Project.objects.filter(resume=resume)
    if request.method == 'POST':

        instance = Project(resume=resume)
        instance.project_name = request.POST.get("project_name", "")
        instance.organization_name = request.POST.get("organization_name", "")
        instance.what_did_you_do = request.POST.get("what_did_you_do", "")
        instance.date = request.POST.get("date", "")
        instance.save()
        return redirect('resume_projects_single', resume_id=resume.id, projects_id=instance.id)
    else:

        instance = None


    context = {"resume_id": resume_id, "templ_type": "projects", "instances": instances, "instance": instance, 'metadata': meta_data_projects}
    return render(request, 'builder.html', context=context)




def projects_single(request, resume_id, projects_id):
    resume = Resume.objects.get(id=resume_id)
    instances = Project.objects.filter(resume=resume)
    if request.method == 'POST':

        instance = Project.objects.filter(resume=resume, id=projects_id)[0]
        instance.project_name = request.POST.get("project_name", "")
        instance.organization_name = request.POST.get("organization_name", "")
        instance.what_did_you_do = request.POST.get("what_did_you_do", "")
        instance.date = request.POST.get("date", "")
        instance.save()

    else:

        instance = Project.objects.filter(resume=resume, id=projects_id)[0]

    context = {"resume_id": resume_id, "templ_type": "projects", "instances": instances, "instance": instance, 'metadata': meta_data_projects}
    return render(request, 'builder.html', context=context)


def projects_delete(request,resume_id, projects_id):
    resume = Resume.objects.get(id=resume_id)
    Project.objects.filter(resume=resume, id=projects_id).delete()

    instance = Project.objects.filter(resume=resume)
    if instance.exists():
        instance = instance[0]
    else:
        instance = None



    if instance != None:
        return redirect('resume_projects_single', resume_id=resume.id, projects_id=instance.id)
    else:
        return redirect('resume_projects', resume_id=resume.id)

