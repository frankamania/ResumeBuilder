from django.http import HttpResponse
from django.shortcuts import render, redirect

from reume.models import Resume, Contact, Socials, Objective, Experience, Education, Skills, Project
from ..meta import meta_data_social

from django.template.loader import render_to_string

def about(request,resume_id):
    resume = Resume.objects.get(id=resume_id)
    if request.method == 'POST':

        if(Contact.objects.filter(resume=resume).exists()):

            instance = Contact.objects.filter(resume=resume)[0]
            instance.firstname = request.POST.get("firstname", "")
            instance.lastname = request.POST.get("lastname", "")
            instance.phonenumber = request.POST.get("phonenumber", "")
            instance.email = request.POST.get("email", "")
            instance.Country = request.POST.get("Country", "")
            instance.State = request.POST.get("State", "")
            instance.City = request.POST.get("City", "")
            instance.save()
        else:

            instance = Contact(resume=resume)
            instance.firstname = request.POST.get("firstname", "")
            instance.lastname = request.POST.get("lastname", "")
            instance.phonenumber = request.POST.get("phonenumber", "")
            instance.email = request.POST.get("email", "")
            instance.Country = request.POST.get("Country", "")
            instance.State = request.POST.get("State", "")
            instance.City = request.POST.get("City", "")
            instance.save()


    else:

        if (Contact.objects.filter(resume=resume).exists()):
            instance = Contact.objects.filter(resume=resume)[0]

        else:
            instance = Contact(resume=resume)
            instance.save()



    context = {"resume_id":resume_id,"templ_type":"abouts","instance":instance}
    return render(request, 'builder.html', context=context)
def socials(request,resume_id):
    resume = Resume.objects.get(id=resume_id)
    if request.method == 'POST':

        if (Socials.objects.filter(resume=resume).exists()):

            instance = Socials.objects.filter(resume=resume)[0]

            instance.linkdin_url =request.POST.get("linkdin_url", "")
            print(request.POST.get("linkdin_url", ""))
            instance.show_linkdin_url = True if request.POST.get("show_linkdin_url", "0") == "1"  else False
            instance.facebook_url = request.POST.get("facebook_url", "")
            instance.show_facebook_url = True if request.POST.get("show_facebook_url", "0") == "1"  else False
            instance.twitter_url = request.POST.get("twitter_url", "")
            instance.show_twitter_url = True if request.POST.get("show_twitter_url", "0") == "1"  else False
            instance.youtube_url = request.POST.get("youtube_url", "")
            instance.show_youtube_url = True if request.POST.get("show_youtube_url", "0") == "1"  else False
            instance.whatsapp_url = request.POST.get("whatsapp_url", "")
            instance.show_whatsapp_url = True if request.POST.get("show_whatsapp_url", "0") == "1"  else False
            instance.telegram_url = request.POST.get("telegram_url", "")
            instance.show_telegram_url = True if request.POST.get("show_telegram_url", "0") == "1"  else False

            instance.save()
        else:

            instance = Socials(resume=resume)
            instance.linkdin_url =request.POST.get("linkdin_url", "")
            instance.show_linkdin_url = True if request.POST.get("show_linkdin_url", "0") == "1"  else False
            instance.facebook_url = request.POST.get("facebook_url", "")
            instance.show_facebook_url = True if request.POST.get("show_facebook_url", "0") == "1"  else False
            instance.twitter_url = request.POST.get("twitter_url", "")
            instance.show_twitter_url = True if request.POST.get("show_twitter_url", "0") == "1"  else False
            instance.youtube_url = request.POST.get("youtube_url", "")
            instance.show_youtube_url = True if request.POST.get("show_youtube_url", "0") == "1"  else False
            instance.whatsapp_url = request.POST.get("whatsapp_url", "")
            instance.show_whatsapp_url = True if request.POST.get("show_whatsapp_url", "0") == "1"  else False
            instance.telegram_url = request.POST.get("telegram_url", "")
            instance.show_telegram_url = True if request.POST.get("show_telegram_url", "0") == "1"  else False

            instance.save()

    else:

        if (Socials.objects.filter(resume=resume).exists()):
            instance = Socials.objects.filter(resume=resume)[0]

        else:
            instance = Socials(resume=resume)
            instance.save()


    context = {"resume_id": resume_id, "templ_type": "socials", "instance": instance,'metadata': meta_data_social}
    return render(request, 'builder.html', context=context)
def objective(request,resume_id):
    
    resume = Resume.objects.get(id=resume_id)
    if request.method == 'POST':

        if (Objective.objects.filter(resume=resume).exists()):

            instance = Objective.objects.filter(resume=resume)[0]
            instance.Objective = request.POST.get("Objective", "")
            instance.save()
        else:

            instance = Objective(resume=resume)
            instance.Objective = request.POST.get("Objective", "")
            instance.save()
    else:

        if (Objective.objects.filter(resume=resume).exists()):

            instance = Objective.objects.filter(resume=resume)[0]

        else:
            instance = Objective(resume=resume)
            instance.save()


    
    context = {"resume_id": resume_id, "templ_type": "Objective", "instance": instance}
    return render(request, 'builder.html', context=context)



def certification(request,resume_id):
    context = {"resume_id": resume_id, "templ_type": "certification", "instance": None}
    return render(request, 'builder.html', context=context)


def coursework(request,resume_id):
    context = {"resume_id": resume_id, "templ_type": "coursework", "instance": None}
    return render(request, 'builder.html', context=context)


def roles(request,resume_id):
    context = {"resume_id": resume_id, "templ_type": "roles", "instance": None}
    return render(request, 'builder.html', context=context)


def skills(request,resume_id):
    context = {"resume_id": resume_id, "templ_type": "skills", "instance": None}
    return render(request, 'builder.html', context=context)


def projects(request,resume_id):
    context = {"resume_id": resume_id, "templ_type": "projects", "instance": None}
    return render(request, 'builder.html', context=context)






