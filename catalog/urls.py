from django.conf.urls import url, include
from  . import views

app_name='catalog'
urlpatterns = [
	url(r'^',views.index, name='catalog'),

	url(r'^product/(?P<product_slug>[-\w]+)/$', views.show_product, name="product"),



]



 

# # (r'^category/(?P<category_slug>[-\w]+)/$', 

# # 'show_category', {

# # 'template_name':'catalog/category.html'},'catalog_category'),


# # (r'^product/(?P<product_slug>[-\w]+)/$', 

# # 'show_product', {

# # 'template_name':'catalog/product.html'},'catalog_product'),

# )










	




	# url(r'^product/(?P<product_slug>[-\w]+)/$', views.show_product, name="product"),
 
 #   ]

# (r'^product/(?P<product_slug>[-\w]+)/$', 
# 'show_product', {
# 'template_name':'catalog/product.html'},'catalog_product'),
# )
