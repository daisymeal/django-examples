from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
	STATUS_CHOICES = (
		('draft','Draft'),
		('published','Published'),
	)	
	title = models.CharField(max_length=250)
	#slug = models.SlugField(max_length=250,unique_for_date='published')
	slug = models.SlugField(max_length=250,default='published')
	author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
	body= models.TextField()
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(default=timezone.now)
	updated = models.DateTimeField(default=timezone.now)
	status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
	class Meta:
		ordering = ('-publish',)#nonexistent field error
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:post_detail',
			args=[self.publish.year,
			self.publish.month,
			self.publish.day,
			self.slug])


class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager,
			self).get_queryset()\
				.filter(status='published')

