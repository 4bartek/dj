from django.shortcuts import render
from .models import Feeds 
from .forms import EditFeeds

from django.contrib.auth.decorators import user_passes_test
from django.db.models import Count


#@user_passes_test(lambda u: u.is_superuser)
def editdb(request):
    form = EditFeeds(request.POST or None, request.FILES or None)
    val = ''
    if form.is_valid():
        db_edit = request.POST['kod']
        print(db_edit)
        if 'get_all_rss' in request.POST:
            if db_edit == 'get':
                try:
                    v = rss_reader()  # same as doing it in another class
                    val = 'Baza pobrana!'
                except:
                    val = 'błąd pobierania bazy!'
            else:
                val = 'nieporawny kod'
                
        elif 'remove_all_rss' in request.POST:      
            if db_edit == 'remove':
                print('removing db ..')
                try:
                    feeds = Feeds.objects.all()
                    feeds.delete()
                    val = 'baza usunięta'
                except:
                    val = 'nie udało się usunąć bazy'
            else:
                val = 'nieporawny kod'
    return render(request, 'rss_editdb.html', {'form': form, 'val':val})




# Create your views here.
def feeds(request):
    rss = Feeds.objects.all()
    #rss = rss_reader()
    return render(request, 'rss_reader.html', {'rss_feeds':rss})



def rss_reader():
    import feedparser
    import re
    from dateutil.parser import parse
    from time import mktime
    from datetime import datetime

    feed_s = []
    url = ['https://bithub.pl/feed/','https://cyfrowaekonomia.pl/feed/','http://bitcoin.pl/?format=feed&type=rss']

    for ur in url:
        
        f = feedparser.parse(ur)

        for e in f['entries']:
            #print(ur)

            if ur == 'https://bithub.pl/feed/':
                img = ((((e.get('summary', '')).split('src="'))[1]).split('"'))[0]
                description = ((e.get('summary', '')).split('<p>'))[1]

            elif ur == 'http://bitcoin.pl/?format=feed&type=rss':
                summary = e.get('summary', '')
                description = (((summary.split('</span></p>'))[-2]).split('" />'))[-1]
                description = description.replace('<br />','')
                description = description.replace('</span>','')
                description = description.replace('<span style="font-size: 12pt;">','')
                img = ((((e.get('summary', '')).split('src="'))[1]).split('"'))[0]
                date = e.published_parsed

            elif ur == 'https://cyfrowaekonomia.pl/feed/':
                description = e.get('summary', '')
                img = ''
            
            description = description.replace('[&#8230;]','...')
            description = description.replace('</p>','')
            description = description.replace('&#8211;','-')
            
            

            source = (ur.split('/'))[2]

            title = e.get('title', '')
            link = e.get('link', '')

            pub = e['published_parsed']
            published = datetime.fromtimestamp(mktime(pub))
            
            feed = Feeds()
    
            try:          
                feed.rss_feed_title = title
            except:
                feed.rss_feed_title = ''

            try:          
                feed.rss_feed_description = description
            except:
                feed.rss_feed_description = ''

            try:          
                feed.rss_feed_img = img
            except:
                feed.rss_feed_img = ''

            try:          
                feed.rss_feed_link = link
            except:
                feed.rss_feed_link = ''

            try:          
                feed.rss_feed_published = published
            except:
                feed.rss_feed_published = ''
            
            try:          
                feed.rss_feed_source = source
            except:
                feed.rss_feed_source = ''

            try:
                feed.pk = None
                print(feed.rss_feed_title)
                feed.save()
            except:
                print('nie udało się zapisać', rss_feed_title)

    #check for duplicates in db
    lastSeenId = float('-Inf')
    rows = Feeds.objects.all().order_by('rss_feed_title')

    for row in rows:
        if row.rss_feed_title == lastSeenId:
            row.delete() # We've seen this id in a previous row
        else: # New id found, save it and check future rows for duplicates.
            lastSeenId = row.rss_feed_title 

    return feed_s