from django.db import models


# Create your models here.

class House(models.Model):
	bariwalar_nam = models.CharField(max_length=100)
	bariwalar_reg_id = models.IntegerField(null=True)
	zilla = models.CharField(max_length=25)
	upazilla = models.CharField(max_length=25)
	elaka = models.CharField(max_length=25)
	family_basha = models.BooleanField(null=True) # True means family basha, False means mess.
	shobar_ghorer_shonkhya = models.IntegerField(null=True)
	bathroomer_shongkhya = models.IntegerField(null=True)
	khabar_ghor = models.BooleanField(null=True)
	rannaghor = models.BooleanField(null=True)
	vara = models.IntegerField(null=True)