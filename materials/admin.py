from django.contrib import admin

from materials.models import Material, Category

admin.site.register(Category)
admin.site.register(Material)