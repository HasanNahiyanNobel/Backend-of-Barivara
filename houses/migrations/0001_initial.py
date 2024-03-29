# Generated by Django 2.2.4 on 2019-09-06 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bariwalar_nam', models.CharField(max_length=100)),
                ('bariwalar_reg_id', models.IntegerField(null=True)),
                ('zilla', models.CharField(max_length=25)),
                ('upazilla', models.CharField(max_length=25)),
                ('elaka', models.CharField(max_length=25)),
                ('family_basha', models.BooleanField(null=True)),
                ('shobar_ghorer_shonkhya', models.IntegerField(null=True)),
                ('bathroomer_shongkhya', models.IntegerField(null=True)),
                ('khabar_ghor', models.BooleanField(null=True)),
                ('rannaghor', models.BooleanField(null=True)),
                ('vara', models.IntegerField(null=True)),
            ],
        ),
    ]
