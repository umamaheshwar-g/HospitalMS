# Generated by Django 3.2 on 2021-08-03 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20210803_0533'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='first_name',
            new_name='name',
        ),
    ]