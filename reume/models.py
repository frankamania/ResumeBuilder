import uuid

from django.db import models

# Create your models here.



class Resume(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(default= 'untitiled reume',null=False)
    template  = models.TextField(default= 'defautl_resume.html',null=False)


class Contact(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, null=False)
    firstname = models.TextField(null=True,default="")
    lastname = models.TextField(null=True,default="")
    email = models.TextField(null=True,default="")
    phonenumber = models.TextField(null=True,default="")
    Country = models.TextField(null=True,default="")
    State = models.TextField(null=True,default="")
    City = models.TextField(null=True,default="")
    CustomFileds = models.JSONField(default=list,null=True)





class Socials(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, null=False)

    #socials
    linkdin_url  = models.TextField(null=True,default="")
    show_linkdin_url  = models.BooleanField(null=False,default=True)
    facebook_url  = models.TextField(null=True,default="")
    show_facebook_url = models.BooleanField(null=False, default=True)
    twitter_url  = models.TextField(null=True,default="")
    show_twitter_url = models.BooleanField(null=False, default=True)
    youtube_url  = models.TextField(null=True,default="")
    show_youtube_url = models.BooleanField(null=False, default=True)
    whatsapp_url  = models.TextField(null=True,default="")
    show_whatsapp_url = models.BooleanField(null=False, default=True)
    telegram_url  = models.TextField(null=True,default="")
    show_telegram_url = models.BooleanField(null=False, default=True)

    CustomFileds = models.JSONField(default=list,null=True)


class Objective(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, null=False)
    Objective = models.TextField(null=False)


class Experience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, null=False)
    compeny_worked_for = models.TextField(null=False)
    your_role = models.TextField(null=False)
    compeny_location = models.TextField(null=False)
    date_from = models.TextField(null=True)
    date_to = models.TextField(null=True)
    what_did_you_do = models.TextField(null=True)


class Project(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, null=False)
    project_name = models.TextField(null=False)
    organization_name = models.TextField(null=True)
    date = models.TextField(null=False)
    what_did_you_do = models.TextField(null=False)


class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, null=False)
    digree_major_qualification = models.TextField(null=False)
    organization_name = models.TextField(null=False)
    organization_location = models.TextField(null=False)
    date = models.TextField(null=False)
    Score = models.TextField(null=True)

class Certicications(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, null=False)
    certificaton_name= models.TextField(null=False)
    certificaton_provider = models.TextField(null=False)
    date = models.TextField(null=False)
    certificaton_About = models.TextField(null=False)

class Cources(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, null=False)
    cource_name= models.TextField(null=False)
    cource_location = models.TextField(null=False)
    date = models.TextField(null=False)
    about_course  = models.TextField(null=False)

class Skills(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, null=False)
    skill = models.TextField(null=False)









