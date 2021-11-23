from django.db import models
from ckeditor.fields import RichTextField

class Contest(models.Model):
	short_name = models.CharField(max_length=5)
	name = models.CharField(max_length=150)
	date = models.DateField()
	start_time = models.DateField()
	length = models.DurationField()
	link = models.URLField(default="localhost")
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.short_name

class Problem(models.Model):
	short_name = models.CharField(max_length=5)
	name = models.CharField(max_length=150)
	ballon_color = models.CharField(max_length=150)
	point = models.SmallIntegerField()
	time_limit = models.SmallIntegerField()
	memory_limit = models.SmallIntegerField()
	description = RichTextField()
	additional_note = RichTextField(blank=True, null=True)
	constraints = RichTextField(blank=True, null=True)
	input_description = RichTextField(blank=True, null=True)
	output_description = RichTextField()
	contest =  models.ForeignKey(Contest, related_name='problems', on_delete=models.SET_NULL, null=True)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.short_name

class SampleInput(models.Model):
	text = RichTextField()
	problem = models.ForeignKey(Problem, related_name='sample_inputs', on_delete=models.CASCADE)

	def __str__(self):
		return f'Sample Input - {self.id }'

class SampleOutput(models.Model):
	text = RichTextField()
	problem = models.ForeignKey(Problem, related_name='sample_outputs', on_delete=models.CASCADE)

	def __str__(self):
		return f'Sample Output - {self.id }'


class Sponsor(models.Model):
	contest = models.ForeignKey(Contest, related_name='sponsors', on_delete=models.CASCADE)
	name = models.CharField(max_length=100)

	def __str__(self):
		return f'{self.contest} - {self.name}'