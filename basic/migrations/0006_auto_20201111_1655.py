# Generated by Django 3.0.5 on 2020-11-11 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0005_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]