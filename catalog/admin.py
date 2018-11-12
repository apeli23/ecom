from django.contrib import admin

# Register your models here.
from .models import Product,category
from .forms import productAdminForm

class productAdmin(admin.ModelAdmin):
	form = productAdminForm

	# sets values for how the admin site lists your products
	fields = ('name','price','slug','old_price','created_at','updated_at',)
	fields_links = ('name',)
	list_per_page = 50
	ordering = ['-created_at']
	search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
	exclude = ('created_at', 'updated_at',)
	
	# sets up slug to be generated from product name
	prepopulated_fields = {'slug' : ('name',)}


	class Meta:
		model = Product
		verbose_name_plural = 'Products'

admin.site.register(Product, productAdmin)

class categoryAdmin(admin.ModelAdmin):
		
	#sets up values for how admin site lists categories
	list_display = ('name', 'created_at', 'updated_at',)
	list_display_links = ('name',)
	list_per_page = 20
	ordering = ['name']
	search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
	exclude = ('created_at', 'updated_at',)

	# sets up slug to be generated from category name
	prepopulated_fields = {'slug' : ('name',)}
	class Meta:
		model = category

admin.site.register(category, productAdmin)