# Generated by Django 3.2.5 on 2021-07-16 06:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('rid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField(default='untitiled reume')),
                ('template', models.TextField(default='defautl_resume.html')),
            ],
        ),
        migrations.CreateModel(
            name='Socials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linkdin_url', models.TextField(default='', null=True)),
                ('show_linkdin_url', models.BooleanField(default=True)),
                ('facebook_url', models.TextField(default='', null=True)),
                ('show_facebook_url', models.BooleanField(default=True)),
                ('twitter_url', models.TextField(default='', null=True)),
                ('show_twitter_url', models.BooleanField(default=True)),
                ('youtube_url', models.TextField(default='', null=True)),
                ('show_youtube_url', models.BooleanField(default=True)),
                ('whatsapp_url', models.TextField(default='', null=True)),
                ('show_whatsapp_url', models.BooleanField(default=True)),
                ('telegram_url', models.TextField(default='', null=True)),
                ('show_telegram_url', models.BooleanField(default=True)),
                ('CustomFileds', models.JSONField(default=list, null=True)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reume.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.TextField()),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reume.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.TextField()),
                ('organization_name', models.TextField(null=True)),
                ('date', models.TextField()),
                ('what_did_you_do', models.TextField()),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reume.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Objective',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Objective', models.TextField()),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reume.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compeny_worked_for', models.TextField()),
                ('your_role', models.TextField()),
                ('compeny_location', models.TextField()),
                ('date_from', models.TextField(null=True)),
                ('date_to', models.TextField(null=True)),
                ('what_did_you_do', models.TextField(null=True)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reume.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('digree_major_qualification', models.TextField()),
                ('organization_name', models.TextField()),
                ('organization_location', models.TextField()),
                ('date', models.TextField()),
                ('Score', models.TextField(null=True)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reume.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Cources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cource_name', models.TextField()),
                ('cource_location', models.TextField()),
                ('date', models.TextField()),
                ('about_course', models.TextField()),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reume.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.TextField(default='', null=True)),
                ('lastname', models.TextField(default='', null=True)),
                ('email', models.TextField(default='', null=True)),
                ('phonenumber', models.TextField(default='', null=True)),
                ('Country', models.TextField(default='', null=True)),
                ('State', models.TextField(default='', null=True)),
                ('City', models.TextField(default='', null=True)),
                ('CustomFileds', models.JSONField(default=list, null=True)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reume.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Certicications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificaton_name', models.TextField()),
                ('certificaton_provider', models.TextField()),
                ('date', models.TextField()),
                ('certificaton_About', models.TextField()),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reume.resume')),
            ],
        ),
    ]
