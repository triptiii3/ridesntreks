# Generated by Django 4.0.6 on 2022-08-23 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='destinations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('destination_title', models.CharField(max_length=100)),
            ],
        ),
    ]
