from django.shortcuts import redirect, render

from reume.models import Resume, Certicications
from ..meta import meta_data_certicications


def certification(request, resume_id):
    resume = Resume.objects.get(id=resume_id)
    instances = Certicications.objects.filter(resume=resume)
    if request.method == 'POST':

        instance = Certicications(resume=resume)
        instance.certificaton_name = request.POST.get("certificaton_name", "")
        instance.certificaton_provider = request.POST.get("certificaton_provider", "")
        instance.date = request.POST.get("date", "")
        instance.certificaton_About = request.POST.get("certificaton_About", "")

        instance.save()
        return redirect('resume_certification_single', resume_id=resume.id, certification_id=instance.id)
    else:

        instance = None


    context = {"resume_id": resume_id, "templ_type": "certification", "instances": instances, "instance": instance , 'metadata': meta_data_certicications}
    return render(request, 'builder.html', context=context,)




def certification_single(request, resume_id, certification_id):
    resume = Resume.objects.get(id=resume_id)
    instances = Certicications.objects.filter(resume=resume)
    if request.method == 'POST':

        instance = Certicications.objects.filter(resume=resume, id=certification_id)[0]
        instance.certificaton_name = request.POST.get("certificaton_name", "")
        instance.certificaton_provider = request.POST.get("certificaton_provider", "")
        instance.date = request.POST.get("date", "")
        instance.certificaton_About = request.POST.get("certificaton_About", "")
        instance.save()

    else:

        instance = Certicications.objects.filter(resume=resume, id=certification_id)[0]

    context = {"resume_id": resume_id, "templ_type": "certification", "instances": instances, "instance": instance, 'metadata': meta_data_certicications}
    return render(request, 'builder.html', context=context)


def certification_delete(request,resume_id, certification_id):
    resume = Resume.objects.get(id=resume_id)
    Certicications.objects.filter(resume=resume, id=certification_id).delete()

    instance = Certicications.objects.filter(resume=resume)
    if instance.exists():
        instance = instance[0]
    else:
        instance = None



    if instance != None:
        return redirect('resume_certification_single', resume_id=resume.id, certification_id=instance.id)
    else:
        return redirect('resume_certification', resume_id=resume.id)

