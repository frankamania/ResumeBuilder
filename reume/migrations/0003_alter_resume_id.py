# Generated by Django 3.2.5 on 2021-07-15 06:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('reume', '0002_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
