# Generated by Django 4.0.6 on 2022-09-02 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_remove_alltrip_inner_video_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='lehtrip',
            fields=[
                ('id', models.AutoField(max_length=50, primary_key=True, serialize=False)),
                ('destination', models.CharField(blank=True, max_length=50, null=True)),
                ('destination_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('mode1', models.CharField(blank=True, max_length=50, null=True)),
                ('mode1_price', models.CharField(blank=True, max_length=50, null=True)),
                ('mode2', models.CharField(blank=True, max_length=50, null=True)),
                ('mode2_price', models.CharField(blank=True, max_length=50, null=True)),
                ('mode3', models.CharField(blank=True, max_length=50, null=True)),
                ('mode3_price', models.CharField(blank=True, max_length=50, null=True)),
                ('mode4', models.CharField(blank=True, max_length=50, null=True)),
                ('mode4_price', models.CharField(blank=True, max_length=50, null=True)),
                ('mode5', models.CharField(blank=True, max_length=50, null=True)),
                ('mode5_price', models.CharField(blank=True, max_length=50, null=True)),
                ('batch1', models.CharField(blank=True, max_length=50, null=True)),
                ('batch2', models.CharField(blank=True, max_length=50, null=True)),
                ('batch3', models.CharField(blank=True, max_length=50, null=True)),
                ('batch4', models.CharField(blank=True, max_length=50, null=True)),
                ('batch5', models.CharField(blank=True, max_length=50, null=True)),
                ('batch6', models.CharField(blank=True, max_length=50, null=True)),
                ('batch7', models.CharField(blank=True, max_length=50, null=True)),
                ('relatedit1', models.CharField(blank=True, max_length=500, null=True)),
                ('reltourimg1', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('relatedtour1', models.CharField(blank=True, max_length=500, null=True)),
                ('relatedprice1', models.CharField(blank=True, max_length=500, null=True)),
                ('relatedit2', models.CharField(blank=True, max_length=500, null=True)),
                ('reltourimg2', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('relatedtour2', models.CharField(blank=True, max_length=500, null=True)),
                ('relatedprice2', models.CharField(blank=True, max_length=500, null=True)),
                ('destination_price', models.CharField(max_length=50)),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('destination_image1', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('destination_image2', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('destination_image3', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('destination_image4', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('destination_image5', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('destination_image6', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('time', models.CharField(blank=True, max_length=50, null=True)),
                ('group', models.CharField(blank=True, max_length=50, null=True)),
                ('hiketype', models.CharField(blank=True, max_length=50, null=True)),
                ('difficulty', models.CharField(blank=True, max_length=50, null=True)),
                ('pickup', models.CharField(blank=True, max_length=50, null=True)),
                ('minage', models.CharField(blank=True, max_length=50, null=True)),
                ('dayno1', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead1', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent1', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno2', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead2', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent2', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno3', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead3', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent3', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno4', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead4', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent4', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno5', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead5', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent5', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno6', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead6', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent6', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno7', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead7', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent7', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno8', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead8', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent8', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno9', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead9', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent9', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno10', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead10', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent10', models.CharField(blank=True, max_length=200, null=True)),
                ('meetingpoint', models.CharField(blank=True, max_length=50, null=True)),
                ('inclusions1', models.CharField(blank=True, max_length=50, null=True)),
                ('inclusions2', models.CharField(blank=True, max_length=50, null=True)),
                ('inclusions3', models.CharField(blank=True, max_length=50, null=True)),
                ('inclusions4', models.CharField(blank=True, max_length=50, null=True)),
                ('inclusions5', models.CharField(blank=True, max_length=50, null=True)),
                ('exclusions1', models.CharField(blank=True, max_length=50, null=True)),
                ('exclusions2', models.CharField(blank=True, max_length=50, null=True)),
                ('exclusions3', models.CharField(blank=True, max_length=50, null=True)),
                ('exclusions4', models.CharField(blank=True, max_length=50, null=True)),
                ('exclusions5', models.CharField(blank=True, max_length=50, null=True)),
                ('expect1', models.CharField(blank=True, max_length=400, null=True)),
                ('expect2', models.CharField(blank=True, max_length=400, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='spititrip',
            fields=[
                ('id', models.AutoField(max_length=50, primary_key=True, serialize=False)),
                ('destination', models.CharField(blank=True, max_length=50, null=True)),
                ('destination_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('mode1', models.CharField(blank=True, max_length=50, null=True)),
                ('mode1_price', models.CharField(blank=True, max_length=50, null=True)),
                ('mode2', models.CharField(blank=True, max_length=50, null=True)),
                ('mode2_price', models.CharField(blank=True, max_length=50, null=True)),
                ('mode3', models.CharField(blank=True, max_length=50, null=True)),
                ('mode3_price', models.CharField(blank=True, max_length=50, null=True)),
                ('mode4', models.CharField(blank=True, max_length=50, null=True)),
                ('mode4_price', models.CharField(blank=True, max_length=50, null=True)),
                ('mode5', models.CharField(blank=True, max_length=50, null=True)),
                ('mode5_price', models.CharField(blank=True, max_length=50, null=True)),
                ('batch1', models.CharField(blank=True, max_length=50, null=True)),
                ('batch2', models.CharField(blank=True, max_length=50, null=True)),
                ('batch3', models.CharField(blank=True, max_length=50, null=True)),
                ('batch4', models.CharField(blank=True, max_length=50, null=True)),
                ('batch5', models.CharField(blank=True, max_length=50, null=True)),
                ('batch6', models.CharField(blank=True, max_length=50, null=True)),
                ('batch7', models.CharField(blank=True, max_length=50, null=True)),
                ('relatedit1', models.CharField(blank=True, max_length=500, null=True)),
                ('reltourimg1', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('relatedtour1', models.CharField(blank=True, max_length=500, null=True)),
                ('relatedprice1', models.CharField(blank=True, max_length=500, null=True)),
                ('relatedit2', models.CharField(blank=True, max_length=500, null=True)),
                ('reltourimg2', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('relatedtour2', models.CharField(blank=True, max_length=500, null=True)),
                ('relatedprice2', models.CharField(blank=True, max_length=500, null=True)),
                ('destination_price', models.CharField(max_length=50)),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('destination_image1', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('destination_image2', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('destination_image3', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('destination_image4', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('destination_image5', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('destination_image6', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('time', models.CharField(blank=True, max_length=50, null=True)),
                ('group', models.CharField(blank=True, max_length=50, null=True)),
                ('hiketype', models.CharField(blank=True, max_length=50, null=True)),
                ('difficulty', models.CharField(blank=True, max_length=50, null=True)),
                ('pickup', models.CharField(blank=True, max_length=50, null=True)),
                ('minage', models.CharField(blank=True, max_length=50, null=True)),
                ('dayno1', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead1', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent1', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno2', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead2', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent2', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno3', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead3', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent3', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno4', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead4', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent4', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno5', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead5', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent5', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno6', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead6', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent6', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno7', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead7', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent7', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno8', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead8', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent8', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno9', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead9', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent9', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno10', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead10', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent10', models.CharField(blank=True, max_length=200, null=True)),
                ('meetingpoint', models.CharField(blank=True, max_length=50, null=True)),
                ('inclusions1', models.CharField(blank=True, max_length=50, null=True)),
                ('inclusions2', models.CharField(blank=True, max_length=50, null=True)),
                ('inclusions3', models.CharField(blank=True, max_length=50, null=True)),
                ('inclusions4', models.CharField(blank=True, max_length=50, null=True)),
                ('inclusions5', models.CharField(blank=True, max_length=50, null=True)),
                ('exclusions1', models.CharField(blank=True, max_length=50, null=True)),
                ('exclusions2', models.CharField(blank=True, max_length=50, null=True)),
                ('exclusions3', models.CharField(blank=True, max_length=50, null=True)),
                ('exclusions4', models.CharField(blank=True, max_length=50, null=True)),
                ('exclusions5', models.CharField(blank=True, max_length=50, null=True)),
                ('expect1', models.CharField(blank=True, max_length=400, null=True)),
                ('expect2', models.CharField(blank=True, max_length=400, null=True)),
            ],
        ),
    ]
