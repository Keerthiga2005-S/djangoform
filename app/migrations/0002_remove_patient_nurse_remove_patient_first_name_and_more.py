# Generated by Django 5.1.3 on 2024-11-22 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='nurse',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='last_name',
        ),
        migrations.AddField(
            model_name='patient',
            name='nurse_first_name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='patient',
            name='nurse_last_name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_first_name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_last_name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='health_issue',
            field=models.TextField(default='Unknown'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='response_to_medication',
            field=models.TextField(blank=True, default='Unknown', null=True),
        ),
        migrations.DeleteModel(
            name='Nurse',
        ),
    ]
