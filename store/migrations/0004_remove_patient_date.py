# Generated by Django 3.2 on 2021-08-03 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='date',
        ),
    ]
