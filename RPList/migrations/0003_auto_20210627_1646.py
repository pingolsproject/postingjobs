# Generated by Django 3.1.6 on 2021-06-27 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RPList', '0002_companyinfo_sstakeholder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyinfo',
            name='company',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='RPList.company'),
        ),
        migrations.AlterField(
            model_name='jobinformation',
            name='companyinfo',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='RPList.companyinfo'),
        ),
        migrations.AlterField(
            model_name='jobrequirements',
            name='jobinformation',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='RPList.jobinformation'),
        ),
        migrations.AlterField(
            model_name='jobstatus',
            name='jobrequirements',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='RPList.jobrequirements'),
        ),
    ]