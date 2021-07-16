from django.shortcuts import redirect, render

from reume.models import Resume, Education
from ..meta import meta_data_education


def education(request, resume_id):
    resume = Resume.objects.get(rid=resume_id)
    instances = Education.objects.filter(resume=resume)
    if request.method == 'POST':

        instance = Education(resume=resume)
        instance.digree_major_qualification = request.POST.get("digree_major_qualification", "")
        instance.organization_name = request.POST.get("organization_name", "")
        instance.organization_location = request.POST.get("organization_location", "")
        instance.date = request.POST.get("date", "")
        instance.Score = request.POST.get("Score", "")

        instance.save()
        return redirect('resume_education_single', resume_id=resume.rid, education_id=instance.id)
    else:

        instance = None


    context = {"resume_id": resume_id, "templ_type": "education", "instances": instances, "instance": instance , 'metadata': meta_data_education}
    return render(request, 'builder.html', context=context,)




def education_single(request, resume_id, education_id):
    resume = Resume.objects.get(rid=resume_id)
    instances = Education.objects.filter(resume=resume)
    if request.method == 'POST':

        instance = Education.objects.filter(resume=resume, id=education_id)[0]
        instance.digree_major_qualification = request.POST.get("digree_major_qualification", "")
        instance.organization_name = request.POST.get("organization_name", "")
        instance.organization_location = request.POST.get("organization_location", "")
        instance.date = request.POST.get("date", "")
        instance.Score = request.POST.get("Score", "")
        instance.save()

    else:

        instance = Education.objects.filter(resume=resume, id=education_id)[0]

    context = {"resume_id": resume_id, "templ_type": "education", "instances": instances, "instance": instance, 'metadata': meta_data_education}
    return render(request, 'builder.html', context=context)


def education_delete(request,resume_id, education_id):
    resume = Resume.objects.get(rid=resume_id)
    Education.objects.filter(resume=resume, id=education_id).delete()

    instance = Education.objects.filter(resume=resume)
    if instance.exists():
        instance = instance[0]
    else:
        instance = None



    if instance != None:
        return redirect('resume_education_single', resume_id=resume.rid, education_id=instance.id)
    else:
        return redirect('resume_education', resume_id=resume.rid)

