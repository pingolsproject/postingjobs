# Generated by Django 3.1.6 on 2021-06-26 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RPList', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyinfo',
            name='Sstakeholder',
            field=models.TextField(default=''),
        ),
    ]