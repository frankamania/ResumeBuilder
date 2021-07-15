from django.shortcuts import redirect, render

from ..meta import meta_data_experience
from reume.models import Resume, Experience


def experience(request, resume_id):
    resume = Resume.objects.get(id=resume_id)
    instances = Experience.objects.filter(resume=resume)
    if request.method == 'POST':

        instance = Experience(resume=resume)
        instance.compeny_worked_for = request.POST.get("compeny_worked_for", "")
        instance.your_role = request.POST.get("your_role", "")
        instance.compeny_location = request.POST.get("compeny_location", "")
        instance.date_from = request.POST.get("date_from", "")
        instance.date_to = request.POST.get("date_to", "")
        instance.what_did_you_do = request.POST.get("what_did_you_do", "")
        instance.save()
        return redirect('resume_experience_single', resume_id=resume.id, experience_id=instance.id)
    else:

        instance = None


    context = {"resume_id": resume_id, "templ_type": "experience", "instances": instances, "instance": instance,'metadata': meta_data_experience}
    return render(request, 'builder.html', context=context)




def experience_single(request, resume_id, experience_id):
    resume = Resume.objects.get(id=resume_id)
    instances = Experience.objects.filter(resume=resume)
    if request.method == 'POST':

        instance = Experience.objects.filter(resume=resume, id=experience_id)[0]
        instance.compeny_worked_for = request.POST.get("compeny_worked_for", "")
        instance.your_role = request.POST.get("your_role", "")
        instance.compeny_location = request.POST.get("compeny_location", "")
        instance.date_from = request.POST.get("date_from", "")
        instance.date_to = request.POST.get("date_to", "")
        instance.what_did_you_do = request.POST.get("what_did_you_do", "")
        instance.save()

    else:

        instance = Experience.objects.filter(resume=resume, id=experience_id)[0]

    context = {"resume_id": resume_id, "templ_type": "experience", "instances": instances, "instance": instance,'metadata': meta_data_experience}
    return render(request, 'builder.html', context=context)


def experience_delete(request,resume_id, experience_id):
    resume = Resume.objects.get(id=resume_id)
    Experience.objects.filter(resume=resume, id=experience_id).delete()

    instance = Experience.objects.filter(resume=resume)
    if instance.exists():
        instance = instance[0]
    else:
        instance = None



    if instance != None:
        return redirect('resume_experience_single', resume_id=resume.id, experience_id=instance.id)
    else:
        return redirect('resume_experience', resume_id=resume.id)

