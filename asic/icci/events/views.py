from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Count
from .models import Event

import requests as r
import json

from .forms import EditEvents


# Create your views here.

#@user_passes_test(lambda u: u.is_superuser)
def events_editdb(request):
    form = EditEvents(request.POST or None, request.FILES or None)
    val = ''
    if form.is_valid():
        db_edit = request.POST['kod']
        print(db_edit)
        if 'get_all_ico' in request.POST:
            if db_edit == 'get':
                try:
                    v = events = get_events()  # same as doing it in another class
                    val = 'Baza pobrana!'
                except:
                    val = 'błąd pobierania bazy!'
            else:
                val = 'nieporawny kod'
                
        elif 'remove_all_ico' in request.POST:      
            if db_edit == 'remove':
                print('removing db ..')
                try:
                    feeds = Event.objects.all()
                    feeds.delete()
                    val = 'baza usunięta'
                except:
                    val = 'nie udało się usunąć bazy'
            else:
                val = 'nieporawny kod'
    return render(request, 'events_editdb.html', {'form': form, 'val':val})

def get_events():
    token = (getToken('906_3e8w8a4nox6ogk0gs8c4k88wsk4o4g4w80c0k8040wcg0csc0k', '6cz6n3bwr2o84g0g04ws8o80coc08cgoss4s4koksw0s4ocg00'))['access_token']
    events = getEvents(token) #pobierz eventsy

def events(request):
    #token = (getToken('906_3e8w8a4nox6ogk0gs8c4k88wsk4o4g4w80c0k8040wcg0csc0k', '6cz6n3bwr2o84g0g04ws8o80coc08cgoss4s4koksw0s4ocg00'))['access_token']
    #events = getEvents(token) #pobierz eventsy
    events = Event.objects.all()
    print('############',events)
    return render(request, 'events.html', {'events':events})

def getToken(id, secret):
    import json
    
    # Get the id and secret from https://api.coinmarketcal.com/developer/register
    payload = {'grant_type': 'client_credentials', 'client_id': id, 'client_secret': secret}
    url = "https://api.coinmarketcal.com/oauth/v2/token"
    try:
        events = r.post(url, data=payload)
        result = json.loads(events.text)
    except json.decoder.JSONDecodeError:
        print("JSONDecodeError")
        result = []
    return result

def getEvents(token, page=None, max=None, dateRangeStart=None, dateRangeEnd=None,
              coins=None, categories=None, sortBy=None, showOnly=None,):
    

    payload = {
            "page": page,
            "max": max,
            "dateRangeStart": dateRangeStart,
            "dateRangeEnd": dateRangeEnd,
            "coins": coins,
            "categories": categories,
            "sortBy": sortBy,
            "showOnly": showOnly,
            'access_token': token,
             }

    url = "https://api.coinmarketcal.com/v1/events"
    try:
        events = r.get(url, params=payload)
        coinmarketcal_events = json.loads(events.text)
    except json.decoder.JSONDecodeError:
        print("JSONDecodeError")
        coinmarketcal_events = ['fetch error']
    
    event = Event()
    
    for e in coinmarketcal_events:
        try:
            event.event_title = e['title']
        except:
            event.event_title = ''
        try:
            event.coins_id = e['coins'][0]['id']
        except:
            event.coins_id = ''
        
        try:
            event.coins_name = e['coins'][0]['name']
        except:
            event.coins_name = ''
        
        try:
            event.coins_symbol = e['coins'][0]['symbol']
        except:
            event.coins_symbol = ''
        
        try:
            event.event_description = e['description']
        except:
            event.event_description = ''
        
        try:
            event.event_proof = e['proof']
        except:
            event.event_proof = ''
        
        try:
            event.event_source = e['source']
        except:
            event.event_source = ''
        
        try:
            event.event_date = e['date_event']
        except:
            event.event_date = ''

        try:
            event.event_created_date = e['created_date']
        except:
            event.event_created_date = ''
        
            event.event_feed_source = 'coinmarketcal.com'
        
        try:
            event.event_is_hot = e['is_hot']
        except:
            event.event_is_hot = False
        
        try:
            event.event_vote_count = e['vote_count']
        except:
            event.event_vote_count =  ''

        try:
            event.event_positive_vote_count = e['positive_vote_count']
        except:
            event.event_positive_vote_count = ''
        
        try:
            event.event_percentage = e['percentage']
        except:
            event.event_percentage = ''
        
        try:
            event.event_event_cat_id = e['categories'][0]['id']
        except:
            event.event_event_cat_id = ''

        try:
            event.event_event_cat_name = e['categories'][0]['name']
        except:
            event.event_event_cat_name = ''

        try:
            event.event_tip_symbol = e['tip_symbol']
        except:
            event.event_tip_symbol = ''

        try:
            event.event_tip_adress = e['tip_adress']
        except:
            event.event_tip_adress = ''

        try:
            event.event_twitter_account = e['twitter_account']
        except:
            event.event_twitter_account = ''

        #save to db
        try:
            event.pk = None
            print(event.event_title)
            event.save()
        except:
            print('nie udało się zapisać', event.event_title)

    #check for duplicates in db
    lastSeenId = float('-Inf')
    rows = Event.objects.all().order_by('event_title')

    for row in rows:
        if row.event_title == lastSeenId:
            row.delete() # We've seen this id in a previous row
        else: # New id found, save it and check future rows for duplicates.
            lastSeenId = row.event_title 


    
