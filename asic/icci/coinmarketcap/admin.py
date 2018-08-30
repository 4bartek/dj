from django.contrib import admin
from .models import Coinmarketcap

# Register your models here.

@admin.register(Coinmarketcap)
class Coinmarketcap(admin.ModelAdmin):
    # fields = ('name', 'description', 'year')
    list_per_page = 400
    list_display = ('cmc_name','cmc_symbol','cmc_rank','cmc_last_updated')
    list_filter = ('cmc_name','cmc_symbol')
    search_fields = ('cmc_name','cmc_symbol')

