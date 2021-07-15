from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .myViews import BuilderViews,ExperianceViews,EductaionViews,CertificationViews,SkillsViews,ProjectViews
urlpatterns = [

    path('', views.home, name='home'),
    path('resume/new', views.create_new_resume, name='create_new_resume'),
    path('resume/<uuid:resume_id>', views.showresume, name='showresume'),

    path('resume/<uuid:resume_id>/about', BuilderViews.about, name='resume_about'),
    path('resume/<uuid:resume_id>/show_resume',views.show_resume, name='resume_show_resume'),
    path('resume/<uuid:resume_id>/finalresume', views.finalresume, name='resume_finalresume'),
    path('resume/<uuid:resume_id>/download_pdf', views.download_pdf, name='resume_download_pdf'),


    path('resume/<uuid:resume_id>/socials', BuilderViews.socials, name='resume_socials'),
    path('resume/<uuid:resume_id>/objective', BuilderViews.objective, name='resume_Objective'),

    path('resume/<uuid:resume_id>/experience', ExperianceViews.experience, name='resume_experience'),
    path('resume/<uuid:resume_id>/experience/<int:experience_id>', ExperianceViews.experience_single, name='resume_experience_single'),
    path('resume/<uuid:resume_id>/experience/<int:experience_id>/delete', ExperianceViews.experience_delete, name='resume_experience_single_delete'),

    path('resume/<uuid:resume_id>/education', EductaionViews.education, name='resume_education'),
    path('resume/<uuid:resume_id>/education/<int:education_id>', EductaionViews.education_single,name='resume_education_single'),
    path('resume/<uuid:resume_id>/education/<int:education_id>/delete', EductaionViews.education_delete,name='resume_education_single_delete'),


    path('resume/<uuid:resume_id>/projects', ProjectViews.projects, name='resume_projects'),
    path('resume/<uuid:resume_id>/projects/<int:projects_id>', ProjectViews.projects_single,name='resume_projects_single'),
    path('resume/<uuid:resume_id>/projects/<int:projects_id>/delete',ProjectViews.projects_delete,name='resume_projects_single_delete'),

    path('resume/<uuid:resume_id>/certification', CertificationViews.certification, name='resume_certification'),
    path('resume/<uuid:resume_id>/certification/<int:certification_id>', CertificationViews.certification_single,name='resume_certification_single'),
    path('resume/<uuid:resume_id>/certification/<int:certification_id>/delete', CertificationViews.certification_delete,name='resume_certification_single_delete'),

    path('resume/<uuid:resume_id>/skills', SkillsViews.skills, name='resume_skills'),
    path('resume/<uuid:resume_id>/skills/<int:skills_id>', SkillsViews.skills_single, name='resume_skills_single'),
    path('resume/<uuid:resume_id>/skills/<int:skills_id>/delete', SkillsViews.skills_delete,name='resume_skills_single_delete'),






]