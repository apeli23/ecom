from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

class category(models.Model):
	class Meta(object):
		"""docstring for Meta"""
		db_table = 'categories'
		ordering = ['-created_at']
		verbose_name_plural= 'Categories'

	name = models.CharField(max_length=50)
	slug = models.SlugField(max_length=50, unique=True, help_text='Unique value of product page URL, created from name.')
	description = models.TextField();
	is_active = models.BooleanField(default=True)
	meta_keywords = models.CharField("Meta Keywords", max_length=255, 
		help_text='Coma-delimited set of SEO keywords for meta tag')
	meta_description = models.CharField("Meta Description", max_length=255,help_text='Content for description  meta tag')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at= models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.name

	
	# @permalink
	def get_absolute_url(self):
		return self.slug

		
					 
			
class Product(models.Model):
	class Meta:
		db_table = 'products'
		ordering = ['-created_at']
		verbose_name_plural= 'Products'
	name = models.CharField(max_length=50, unique=True)
	slug = models.SlugField(max_length=50, unique=True, help_text='Unique value of product page URL, created from name.')
	brand = models.CharField(max_length=50)
	sku = models.CharField(max_length=50)
	price = models.DecimalField(max_digits=9,decimal_places=2, blank=True,default=0.00)
	old_price = models.DecimalField(max_digits=9,decimal_places=2, blank=True,default=0.00)
	image = models.CharField(max_length=50)
	is_active = models.BooleanField(default=True)
	is_bestseller = models.BooleanField(default=False)
	is_featured =  models.BooleanField(default=False)
	quantity = models.IntegerField()
	description = models.TextField()
	meta_keywords = models.CharField("Meta Keywords", max_length=255, 
		help_text='Coma-delimited set of SEO keywords for meta tag')
	
	meta_description = models.CharField("Meta Description", max_length=255,help_text='Content for description  meta tag')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	categories = models.ManyToManyField(category)
	
	def __str__(self):
		return self.name

	# @permalink
	def get_absolute_url(self):
		return self.slug

			
			
	 
	 
	 
	# def get_absolute_url(self):
		
	# 	return ('catalog_product', (), { 'product_slug': self.slug })

	def sale_price(self):
		if self.old_price > self.price:
			return self.price

		else:
			return None

	