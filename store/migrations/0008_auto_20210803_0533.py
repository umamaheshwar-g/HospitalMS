# Generated by Django 3.2 on 2021-08-03 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_patient_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=200)),
                ('doctor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='store.doctor')),
            ],
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]
