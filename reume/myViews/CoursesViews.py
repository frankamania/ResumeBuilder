from django.shortcuts import redirect, render

from reume.models import Resume, Cources


def coursework(request, resume_id):
    resume = Resume.objects.get(rid=resume_id)
    instances = Cources.objects.filter(resume=resume)
    if request.method == 'POST':

        instance = Cources(resume=resume)
        instance.cource_name = request.POST.get("cource_name", "")
        instance.cource_location = request.POST.get("cource_location", "")
        instance.date = request.POST.get("date", "")
        instance.about_course = request.POST.get("about_course", "")
        instance.save()
        return redirect('resume_coursework_single', resume_id=resume.rid, coursework_id=instance.id)
    else:

        instance = None


    context = {"resume_id": resume_id, "templ_type": "coursework", "instances": instances, "instance": instance}
    return render(request, 'builder.html', context=context)




def coursework_single(request, resume_id, coursework_id):
    resume = Resume.objects.get(rid=resume_id)
    instances = Cources.objects.filter(resume=resume)
    if request.method == 'POST':

        instance = Cources.objects.filter(resume=resume, id=coursework_id)[0]
        instance.cource_name = request.POST.get("cource_name", "")
        instance.cource_location = request.POST.get("cource_location", "")
        instance.date = request.POST.get("date", "")
        instance.about_course = request.POST.get("about_course", "")
        instance.save()

    else:

        instance = Cources.objects.filter(resume=resume, id=coursework_id)[0]

    context = {"resume_id": resume_id, "templ_type": "coursework", "instances": instances, "instance": instance}
    return render(request, 'builder.html', context=context)


def coursework_delete(request,resume_id, coursework_id):
    resume = Resume.objects.get(rid=resume_id)
    Cources.objects.filter(resume=resume, id=coursework_id).delete()

    instance = Cources.objects.filter(resume=resume)
    if instance.exists():
        instance = instance[0]
    else:
        instance = None



    if instance != None:
        return redirect('resume_coursework_single', resume_id=resume.rid, coursework_id=instance.id)
    else:
        return redirect('resume_coursework', resume_id=resume.rid)

