from django.shortcuts import get_object_or_404, render
from catalog.models import category, Product
from django.template import RequestContext

# Create your views here.

#check lines 13, 33
def index(request):
	page_title = 'clothes and shoes'
	context = {'page_title':page_title}
	template = 'index.html'
	
	return render(request,template,context)



# def index(request, template_name="catalog/index.html"):
# page_title = 'Musical Instruments and Sheet Music for Musicians'
# return render_to_response(template_name, locals(),
# context_instance=RequestContext(request))


# def index(request):
# 	page_title = 'clothes and shoes'
# 	context = {'page_title':page_title}
# 	template = 'catalog/index.html'
	 	
# 	return render(request,template,context),
	 

def show_category(request, category_slug, template="catalog/category.html"):
	
	c = get_object_or_404(Category, slug=category_slug)#hope u get this idea
	
	products = c.product_set.all()
	page_title = c.name
	meta_keywords = c.meta_keywords
	meta_description = c.meta_description
	
	return render(template, locals(), 
	context_instance=RequestContext(request))

def show_product(request, product_slug, template="catalog/product.html"):
	p = get_object_or_404(Product, slug=product_slug)
	categories = p.categories.filter(is_active=True)
	page_title = p.name
	meta_keywords = p.meta_keywords
	meta_description = p.meta_description
	
	return render(template, locals(),
	context_instance=RequestContext(request))