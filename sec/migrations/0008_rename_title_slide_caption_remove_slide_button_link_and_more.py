# Generated by Django 4.2.5 on 2024-06-19 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sec', '0007_slide_delete_sliderimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slide',
            old_name='title',
            new_name='caption',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='button_link',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='button_text',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='description',
        ),
    ]
