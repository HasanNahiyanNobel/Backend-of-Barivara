# Generated by Django 2.2.4 on 2019-09-05 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='bariwalar_reg_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='house',
            name='family_basha',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='house',
            name='bathroomer_shongkhya',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='house',
            name='khabar_ghor',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='house',
            name='rannaghor',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='house',
            name='shobar_ghorer_shonkhya',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='house',
            name='vara',
            field=models.IntegerField(default=0),
        ),
    ]
