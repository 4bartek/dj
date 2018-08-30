from django.shortcuts import render
from .models import IcoEvent
from .forms import EditIco

from django.contrib.auth.decorators import user_passes_test
from django.db.models import Count

# Create your views here.

#@user_passes_test(lambda u: u.is_superuser)
def ico_editdb(request):
    form = EditIco(request.POST or None, request.FILES or None)
    val = ''
    if form.is_valid():
        db_edit = request.POST['kod']
        print(db_edit)
        if 'get_all_ico' in request.POST:
            if db_edit == 'get':
                try:
                    v = ico_fetch()  # same as doing it in another class
                    val = 'Baza pobrana!'
                except:
                    val = 'błąd pobierania bazy!'
            else:
                val = 'nieporawny kod'
                
        elif 'remove_all_ico' in request.POST:      
            if db_edit == 'remove':
                print('removing db ..')
                try:
                    feeds = IcoEvent.objects.all()
                    feeds.delete()
                    val = 'baza usunięta'
                except:
                    val = 'nie udało się usunąć bazy'
            else:
                val = 'nieporawny kod'
    return render(request, 'ico_editdb.html', {'form': form, 'val':val})





def ico(request):
    #all_ico = ico_fetch()
    ### nie działa
    ico_live = IcoEvent.objects.filter(ico_typ="live")
    ico_upcoming = IcoEvent.objects.filter(ico_typ="upcoming")
    ico_finished = IcoEvent.objects.filter(ico_typ="finished")
    ###

    return render(request, 'ico.html', {
        'ico_live':ico_live, 
        'ico_upcoming':ico_upcoming,
        'ico_finished': ico_finished,
        })

def ico_fetch():

    import requests
    import json

    ico_req = requests.get("https://api.icowatchlist.com/public/v1/all")
    ico_req = json.loads(ico_req.content)
    
    ico_live = ico_req['ico']['live']
    ico_upcoming = ico_req['ico']['upcoming']
    ico_finished = ico_req['ico']['finished']


    ico = IcoEvent()
    for x in ico_live:
        print(x)

    
    for i in ico_upcoming:
        try:          
            ico.ico_title = i['name']
        except:
            ico.ico_title = ''
        try:          
            ico.ico_description = i['description']
        except:
            ico.ico_description = ''
        try:          
            ico.ico_img = i['image']
        except:
            ico.ico_img = ''
        try:          
            ico.ico_website_link = str(i['website_link']) #brak
        except:
            ico.ico_website_link = ''
        try:          
            ico.ico_start_time = i['start_time']
        except:
            ico.ico_start_time = ''
        try:          
            ico.ico_end_time = i['end_time']
        except:
            ico.ico_end_time = ''
        try:          
            ico.ico_icowatchlist_url = i['icowatchlist_url']#brak
        except:
            ico.ico_icowatchlist_url = ''
        try:          
            ico.ico_source = 'icowatchlist.com'
        except:
            ico.ico_source = ''
        try:          
            ico.ico_typ = 'live'
        except:
            ico.ico_typ = ''
        
        try:
            ico.pk = None
            print(ico.ico_website_link)
            ico.save()
        except:
            print('nie udało się zapisać', ico.ico_title)


    for i in ico_live:
        try:          
            ico.ico_title = i['name']
        except:
            ico.ico_title = ''
        try:          
            ico.ico_description = i['description']
        except:
            ico.ico_description = ''
        try:          
            ico.ico_img = i['image']
        except:
            ico.ico_img = ''
        try:          
            ico.ico_website_link = str(i['website_link']) #brak
        except:
            ico.ico_website_link = ''
        try:          
            ico.ico_start_time = i['start_time']
        except:
            ico.ico_start_time = ''
        try:          
            ico.ico_end_time = i['end_time']
        except:
            ico.ico_end_time = ''
        try:          
            ico.ico_icowatchlist_url = i['icowatchlist_url']#brak
        except:
            ico.ico_icowatchlist_url = ''
        try:          
            ico.ico_source = 'icowatchlist.com'
        except:
            ico.ico_source = ''
        try:          
            ico.ico_typ = 'upcoming'
        except:
            ico.ico_typ = ''
        
        try:
            ico.pk = None
            print(ico.ico_website_link)
            ico.save()
        except:
            print('nie udało się zapisać', ico.ico_title)

    for i in ico_finished:
        try:          
            ico.ico_title = i['name']
        except:
            ico.ico_title = ''
        try:          
            ico.ico_description = i['description']
        except:
            ico.ico_description = ''
        try:          
            ico.ico_img = i['image']
        except:
            ico.ico_img = ''
        try:          
            ico.ico_website_link = str(i['website_link']) #brak
        except:
            ico.ico_website_link = ''
        try:          
            ico.ico_start_time = i['start_time']
        except:
            ico.ico_start_time = ''
        try:          
            ico.ico_end_time = i['end_time']
        except:
            ico.ico_end_time = ''
        try:          
            ico.ico_icowatchlist_url = i['icowatchlist_url']#brak
        except:
            ico.ico_icowatchlist_url = ''
        try:          
            ico.ico_source = 'icowatchlist.com'
        except:
            ico.ico_source = ''
        try:          
            ico.ico_typ = 'finished'
        except:
            ico.ico_typ = ''
        
        try:
            ico.pk = None
            print(ico.ico_website_link)
            ico.save()
        except:
            print('nie udało się zapisać', ico.ico_title)


    #check for duplicates in db
    lastSeenId = float('-Inf')
    rows = IcoEvent.objects.all().order_by('ico_title')

    for row in rows:
        if row.ico_title == lastSeenId:
            row.delete() # We've seen this id in a previous row
        else: # New id found, save it and check future rows for duplicates.
            lastSeenId = row.ico_title 


    return {
        'ico_live':ico_live,
        'ico_upcoming':ico_upcoming,
        'ico_finished':ico_finished}



    