'''
linki strony:
strona główna (home.html)- 
http://127.0.0.1:8000/  

ICO:
http://127.0.0.1:8000/ico/
http://127.0.0.1:8000/ico/ico_editdb/

VIDEO:
http://127.0.0.1:8000/video/
http://127.0.0.1:8000/video/editdb/

EVENTS (KALENDARZ)
http://127.0.0.1:8000/events/
http://127.0.0.1:8000/events/events_editdb/

RSS:
http://127.0.0.1:8000/rss_reader/
http://127.0.0.1:8000/rss_reader/rss_editdb/

na stronach znajdziesz opis jak korzystać z poszczególnych aplikacji
'''


from django.shortcuts import render
from events.models import Event
from ico.models import IcoEvent
from video.models import Movie
from rss_reader.models import Feeds
from coinmarketcap.models import Coinmarketcap



# Create your views here.
def home(request):
    
    # kalendarz
    events = Event.objects.all()

    # ico 
    ico_live = IcoEvent.objects.filter(ico_typ="live")
    ico_upcoming = IcoEvent.objects.filter(ico_typ="upcoming")
    ico_finished = IcoEvent.objects.filter(ico_typ="finished")
    
    # video
    video = Movie.objects.all()

    # rss
    rss_feeds = Feeds.objects.all()

    # coinmarket
    coinmarketcap = Coinmarketcap.objects.all()
    cmc_BTC = Coinmarketcap.objects.filter(cmc_name="Bitcoin")


    
    return render(request, 'home.html', {
        'events':events[0:5],
        'ico_live':ico_live[0:5], 
        'ico_upcoming':ico_upcoming,
        'ico_finished': ico_finished[0:5],
        'filmy': video[0:14], 
        'filmy1': video[0:14], 
        'rss_feeds': rss_feeds[3:37],       
        'coinmarketcap': coinmarketcap[2:12],
        'coinmarketcap1': cmc_BTC,      
        })



    '''
    w return przekazujemy klucz np.
    'events' i wartość events[] (opcjonalnie mozna dodać kwadratowy nawias)
    
    [0:4] oznacza ze ma wziąć 4 pierwsze elementy ze zbioru
    [5:10] od piątego do dziesiątego itd.
    
    nazwa w '' oznacza pod jaką zmienną zostaną przekazane nasze elementy do pliku html.
    
    w przypadku:                        'events':events[0:5]

    będziemy mogli uzyć zmiennej:       events w  {% for x in events %}

    #

    mozesz tworzyć rózne nazwy w '' jednak nazwa wartości (:events) musi być bez zmian np:
    
    'events10':events[0:10]
    
    przekaze ci zmienna events10 do pliku home.html i będziesz mógł

    {% for x in events10 %}

    w ten sposób pobierzesz 10 wpisów z bazy
    bez nawiasu pobierze wszystkie elementy
    '''


    '''
    w taki sposób mozna odfiltrowac dane po kategorii:

    ico_live = IcoEvent.objects.filter(ico_typ="live")
    ico_upcoming = IcoEvent.objects.filter(ico_typ="upcoming")
    ico_finished = IcoEvent.objects.filter(ico_typ="finished")
    '''

                



