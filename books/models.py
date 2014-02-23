from django.db import models


class Publisher(models.Model):
	name = models.CharField(max_length=100)

class Author(models.Model):
	name = models.CharField(max_length=100)

class Book(models.Model):
	authors = models.ManyToManyField(Author)
	title = models.CharField(max_length=125)
	publisher = models.ForeignKey(Publisher)
	publish_date = models.DateField()

