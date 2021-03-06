# Generated by Django 2.1 on 2018-08-29 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GetIco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kod', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='IcoEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ico_title', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('ico_description', models.TextField(blank=True, default='', null=True)),
                ('ico_img', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('ico_website_link', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('ico_start_time', models.DateTimeField(blank=True, null=True)),
                ('ico_end_time', models.DateTimeField(blank=True, null=True)),
                ('ico_icowatchlist_url', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('ico_source', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('ico_typ', models.CharField(blank=True, default='', max_length=10, null=True)),
            ],
        ),
    ]
