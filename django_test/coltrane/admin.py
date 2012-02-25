from django.contrib import admin
from coltrane.models import Category, Entry

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = { 'slug': ['title'] }
	pass

class EntryAdmin(admin.ModelAdmin):
	prepopulated_fields = { 'slug': ['title'] }
	pass

admin.site.register(Entry, EntryAdmin)
admin.site.register(Category, CategoryAdmin)

