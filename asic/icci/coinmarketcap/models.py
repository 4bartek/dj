from django.db import models

# Create your models here.
class Coinmarketcap(models.Model):
    cmc_coin_id = models.CharField(max_length=128, default='',null=True, blank=True)
    cmc_name = models.CharField(max_length=128, default='',null=True, blank=True)
    cmc_symbol = models.CharField(max_length=128, default='',null=True, blank=True)
    cmc_rank = models.CharField(max_length=128, default='',null=True, blank=True)
    cmc_price_usd = models.CharField(max_length=128, default='',null=True, blank=True)
    cmc_price_btc = models.CharField(max_length=128, default='',null=True, blank=True)
    cmc_price_pln = models.CharField(max_length=128, default='',null=True, blank=True)
    cmc_capitalization = models.CharField(max_length=128, default='',null=True, blank=True) 
    cmc_volume_usd_24h = models.CharField(max_length=128, default='',null=True, blank=True)
    cmc_capitalization_pln = models.CharField(max_length=128, default='',null=True, blank=True)
    cmc_market_cap_usd = models.CharField(max_length=128, default='',null=True, blank=True)
    cmc_available_supply = models.CharField(max_length=128, default='',null=True, blank=True)
    cmc_total_supply = models.CharField(max_length=128, default='',null=True, blank=True)
    cmc_max_supply = models.CharField(max_length=128, default='',null=True, blank=True)
    cmc_percent_change_1h = models.CharField(max_length=12, default='',null=True, blank=True)
    cmc_percent_change_24h = models.CharField(max_length=12, default='',null=True, blank=True)
    cmc_percent_change_7d = models.CharField(max_length=12, default='',null=True, blank=True) 
    cmc_last_updated = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name_with_year()

    def name_with_year(self):
        return str(self.cmc_name)

class EditCoinmarketcap(models.Model):
    kod = models.CharField(max_length=128)