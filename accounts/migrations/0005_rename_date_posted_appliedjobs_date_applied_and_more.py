# Generated by Django 4.0.4 on 2022-05-18 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_studentprofile_cv_alter_postjob_company_appliedjobs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appliedjobs',
            old_name='date_posted',
            new_name='date_applied',
        ),
        migrations.AddField(
            model_name='appliedjobs',
            name='certificate',
            field=models.CharField(blank=True, choices=[('Phd', 'Phd'), ('diploma', 'diploma'), ('degreee', 'degreee')], max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='appliedjobs',
            name='experience',
            field=models.TextField(blank=True, null=True),
        ),
    ]
