# Generated by Django 4.0.2 on 2022-07-22 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioPage', '0007_alter_projects_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]