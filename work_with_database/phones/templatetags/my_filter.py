from django import template
from phones.models import Phone

register = template.Library()

@register.filter(name='times') 
def times(number):
	return range(number)

@register.filter(name='arind') 
def arind(ar: list, ind: int = 0) -> str:
	a = ar[ind]
	return str(a)

@register.filter(name='obj_name')
def obj_name(obj, ind:int = -1):
	if ind == -1:
		return obj.name
	return obj[ind].name

@register.filter(name='obj_image')
def obj_image(obj, ind:int = -1):
	if ind == -1:
		return obj.image
	return obj[ind].image

@register.filter(name='obj_price')
def obj_price(obj, ind:int = -1):
	if ind == -1:
		return obj.price
	return obj[ind].price

@register.filter(name='obj_slug')
def obj_slug(obj, ind:int = -1):
	if ind == -1:
		return obj.slug
	return obj[ind].slug

@register.filter(name='obj_release_date')
def obj_release_date(obj, ind:int = -1):
	if ind == -1:
		return obj.release_date
	return obj[ind].release_date

@register.filter(name='obj_lte_exists')
def obj_lte_exists(obj, ind:int = -1):
	if ind == -1:
		return obj.lte_exists
	return obj[ind].lte_exists