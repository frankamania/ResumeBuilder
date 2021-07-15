from django.contrib import admin

# Register your models here.

from . models import Resume,Project,Contact,Education,Experience,Cources,Certicications,Objective,Socials

admin.site.register(Resume)
admin.site.register(Project)
admin.site.register(Contact)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Cources)
admin.site.register(Certicications)
admin.site.register(Objective)
admin.site.register(Socials)

