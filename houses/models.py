from django.db import models


# Create your models here.

class House(models.Model):
	bariwalar_nam = models.CharField(max_length=100)
	bariwalar_reg_id = models.IntegerField
	zilla = models.CharField(max_length=50)
	upazilla = models.CharField(max_length=50)
	elaka = models.CharField(max_length=50)
	bashar_dhoron = models.BooleanField
	shobar_ghorer_shonkhya = models.IntegerField
	bathroomer_shongkhya = models.IntegerField
	khabar_ghor = models.BooleanField
	rannaghor = models.BooleanField
	vara = models.IntegerField