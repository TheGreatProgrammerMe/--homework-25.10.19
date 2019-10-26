from django.db import models
from django.contrib import admin

class Phone(models.Model):
    id = models.PositiveIntegerField(primary_key = True)
    name = models.TextField()
    image = models.TextField()
    price = models.DecimalField(
    	max_digits = 7,
    	decimal_places = 2
    )
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()

class PhoneAdmin(admin.ModelAdmin):
	pass

admin.site.register(Phone,PhoneAdmin)