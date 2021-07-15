from django.shortcuts import redirect, render

from reume.models import Resume, Skills
from ..meta import meta_data_skills


def skills(request, resume_id):
    resume = Resume.objects.get(id=resume_id)
    instances = Skills.objects.filter(resume=resume)
    if request.method == 'POST':

        instance = Skills(resume=resume)
        instance.skill = request.POST.get("skill", "")
        instance.save()
        return redirect('resume_skills_single', resume_id=resume.id, skills_id=instance.id)
    else:

        instance = None


    context = {"resume_id": resume_id, "templ_type": "skills", "instances": instances, "instance": instance , 'metadata': meta_data_skills}
    return render(request, 'builder.html', context=context,)




def skills_single(request, resume_id, skills_id):
    resume = Resume.objects.get(id=resume_id)
    instances = Skills.objects.filter(resume=resume)
    if request.method == 'POST':

        instance = Skills.objects.filter(resume=resume, id=skills_id)[0]
        instance.skill = request.POST.get("skill", "")
        instance.save()

    else:

        instance = Skills.objects.filter(resume=resume, id=skills_id)[0]

    context = {"resume_id": resume_id, "templ_type": "skills", "instances": instances, "instance": instance, 'metadata': meta_data_skills}
    return render(request, 'builder.html', context=context)


def skills_delete(request,resume_id, skills_id):
    resume = Resume.objects.get(id=resume_id)
    Skills.objects.filter(resume=resume, id=skills_id).delete()

    instance = Skills.objects.filter(resume=resume)
    if instance.exists():
        instance = instance[0]
    else:
        instance = None



    if instance != None:
        return redirect('resume_skills_single', resume_id=resume.id, skills_id=instance.id)
    else:
        return redirect('resume_skills', resume_id=resume.id)

