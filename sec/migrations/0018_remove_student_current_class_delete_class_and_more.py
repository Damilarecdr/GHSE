# Generated by Django 4.2.5 on 2024-06-20 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sec', '0017_class_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='current_class',
        ),
        migrations.DeleteModel(
            name='Class',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
