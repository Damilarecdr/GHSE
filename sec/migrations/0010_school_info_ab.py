# Generated by Django 4.2.5 on 2024-06-20 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sec', '0009_school_info_delete_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='school_info',
            name='ab',
            field=models.CharField(default='exist', max_length=10),
            preserve_default=False,
        ),
    ]
