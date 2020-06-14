from django.contrib import admin
from .models import Listings

# Register your models here.
class LisitngsAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'is_published', 'price')
    list_link=('id',)
    list_filter=('realtor',)
    list_editable=('is_published',)
    search_fields=('price','zipcode')
    list_perpage = 25


admin.site.register(Listings,LisitngsAdmin)


