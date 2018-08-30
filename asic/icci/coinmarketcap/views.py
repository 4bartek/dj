from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Count
from .models import Coinmarketcap
# Create your views here.
from .forms import EditCoinmarketcap


def coinmarketcap(request):
    #coinmarketcap = get_coinmarketcap_data()
    coinmarketcap = Coinmarketcap.objects.all()
    print('############',coinmarketcap)
    return render(request, 'coinmarketcap.html', {'coinmarketcap':coinmarketcap})

def get_coinmarketcap_data():
    import ccxt
    import datetime
    import urllib.request, json 
    coinmarketcap = Coinmarketcap()

    with urllib.request.urlopen("https://panel.walutomat.pl/api/v1/best_offers.php?curr1=USD&curr2=PLN") as url:
        daneWalutomat = json.loads(url.read().decode())

    walutomat_buy_USD_PLN = float(daneWalutomat['buy'])

    zbior_rynkow_lista = []

    gielda = 'coinmarketcap'
    exchange = eval('ccxt.'+gielda+'()')
    exchange.load_markets()
    rynki = (exchange.fetchTickers()).values()

    for rynek in rynki:
        info = rynek['info']    
        coinmarketcap.cmc_name = info['name']
        coinmarketcap.cmc_symbol = info['symbol']
        coinmarketcap.cmc_rank = info['rank']
        coinmarketcap.cmc_price_usd = info['price_usd']
        coinmarketcap.cmc_market_cap_usd = info['market_cap_usd']
        coinmarketcap.cmc_coin_id = info['id']
        coinmarketcap.cmc_price_btc = info['price_btc']
        coinmarketcap.cmc_volume_usd_24h = info['24h_volume_usd']
        coinmarketcap.cmc_available_supply = info['available_supply']
        coinmarketcap.cmc_available_supply = info['available_supply']
        coinmarketcap.cmc_total_supply = info['total_supply']
        coinmarketcap.cmc_max_supply = info['max_supply']
        coinmarketcap.cmc_percent_change_1h = info['percent_change_1h']
        coinmarketcap.cmc_percent_change_24h = info['percent_change_24h']
        coinmarketcap.cmc_percent_change_7d = info['percent_change_7d']
        coinmarketcap.cmc_last_updated = info['last_updated']

        if coinmarketcap.cmc_price_usd == None:
            coinmarketcap.cmc_price_usd = 0

        coinmarketcap.cmc_price_pln = float(coinmarketcap.cmc_price_usd) * float(walutomat_buy_USD_PLN)

        if coinmarketcap.cmc_price_btc == None:
            coinmarketcap.cmc_price_btc = 0

        if coinmarketcap.cmc_volume_usd_24h == None:
            coinmarketcap.cmc_volume_usd_24h = 0

        if coinmarketcap.cmc_available_supply == None:
            coinmarketcap.cmc_available_supply = 0

        if coinmarketcap.cmc_total_supply == None:
            coinmarketcap.cmc_total_supply = 0

        if coinmarketcap.cmc_max_supply == None:
            coinmarketcap.cmc_max_supply = 0

        if coinmarketcap.cmc_percent_change_1h == None:
            coinmarketcap.cmc_percent_change_1h = 0

        if coinmarketcap.cmc_percent_change_24h == None:
            coinmarketcap.cmc_percent_change_24h = 0

        if coinmarketcap.cmc_percent_change_7d == None:
            coinmarketcap.cmc_percent_change_7d = 0

        if coinmarketcap.cmc_last_updated == None:
            coinmarketcap.cmc_last_updated = '2001-01-01T01:01:01.000Z'
        else:
            coinmarketcap.cmc_last_updated = datetime.datetime.fromtimestamp(int(coinmarketcap.cmc_last_updated))

        if coinmarketcap.cmc_available_supply != None and coinmarketcap.cmc_price_btc != None:
            coinmarketcap.cmc_capitalization = round(float(coinmarketcap.cmc_available_supply) * float(coinmarketcap.cmc_price_usd),0)
        else:
            coinmarketcap.cmc_capitalization = 0  
        
        if coinmarketcap.cmc_available_supply != None and coinmarketcap.cmc_price_btc != None:
            coinmarketcap.cmc_capitalization_pln = round(float(coinmarketcap.cmc_available_supply) * float(coinmarketcap.cmc_price_usd) * walutomat_buy_USD_PLN,0)
        else:
            coinmarketcap.cmc_capitalization_pln = 0
        try:
            coinmarketcap.pk = None
            coinmarketcap.save()
        except:
            print('nie udało się zapisać', coinmarketcap.cmc_name)

    #check for duplicates in db
    lastSeenId = float('-Inf')
    rows = Coinmarketcap.objects.all().order_by('cmc_name')
    for row in rows:
        if row.cmc_name == lastSeenId:
            row.delete() # We've seen this id in a previous row
        else: # New id found, save it and check future rows for duplicates.
            lastSeenId = row.cmc_name 



#@user_passes_test(lambda u: u.is_superuser)
def coinmarketcap_editdb(request):
    form = EditCoinmarketcap(request.POST or None, request.FILES or None)
    val = ''
    if form.is_valid():
        db_edit = request.POST['kod']
        print(db_edit)
        if 'get_all_coinmarketdata' in request.POST:
            if db_edit == 'get':
                try:
                    v = events = get_coinmarketcap_data()  # same as doing it in another class
                    val = 'Baza pobrana!'
                except:
                    val = 'błąd pobierania bazy!'
            else:
                val = 'nieporawny kod'
                
        elif 'remove_all_coinmarketdata' in request.POST:      
            if db_edit == 'remove':
                print('removing db ..')
                try:
                    cmc = Coinmarketcap.objects.all()
                    cmc.delete()
                    val = 'baza usunięta'
                except:
                    val = 'nie udało się usunąć bazy'
            else:
                val = 'nieporawny kod'
    return render(request, 'coinmarketcap_editdb.html', {'form': form, 'val':val})