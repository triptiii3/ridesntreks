# Generated by Django 4.0.6 on 2022-08-24 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_rename_bikingtours_bikingtrip'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='backpackingtours',
            new_name='backpackingtrip',
        ),
        migrations.RenameModel(
            old_name='roadtours',
            new_name='roadtrip',
        ),
        migrations.RenameModel(
            old_name='weekendtours',
            new_name='weekendtrip',
        ),
    ]
