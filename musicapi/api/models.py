from django.db import models
from model_utils.models import TimeStampedModel

class Music(TimeStampedModel):
	class Meta:
		db_table = 'music'
	
	title = models.CharField(max_length=200)
	seconds = models.IntegerField()

	def __str__(self):
		return self.title

class Band(TimeStampedModel):
	class Meta:
		db_table = 'band'

	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Album(TimeStampedModel):
	class Meta:
		db_table = 'album'
	
	title = models.CharField(max_length=200)
	band = models.ForeignKey(Band, on_delete=models.CASCADE)
	date = models.DateField()

	def __str__(self):
		return self.title

class Member(models.Model):
	class Meta:
		db_table = 'member'
	
	name = models.CharField(max_length=200)
	age = models.IntegerField()
	band = models.ForeignKey('Band', related_name='members', on_delete=models.CASCADE)

	def __str__(self):
		return self.name
