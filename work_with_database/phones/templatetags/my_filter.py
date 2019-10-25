from django import template

register = template.Library()

@register.filter(name='times') 
def times(number):
	return range(number)

@register.filter(name='arind') 
def arind(ar: list, ind: int = 0) -> str:
	a = ar[ind]
	return str(a)
	