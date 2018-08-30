from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Movie
from .forms import MovieForm, AllMoviesForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer, MovieSerializer
from django.db.models import Count


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

def wszystkie_filmy(request):
    filmy = Movie.objects.all()
    return render(request, 'lista_filmow.html', {'filmy': filmy})


#################################
#                               #
#       Add videos to db        #
#                               #
#################################

#@user_passes_test(lambda u: u.is_superuser)
def editdb(request):
    form = AllMoviesForm(request.POST or None, request.FILES or None)
    val = ''
    if form.is_valid():
        db_edit = request.POST['kod']
        print(db_edit)
        if 'get_all_videos' in request.POST:
            if db_edit == 'get':
                try:
                    v = Video_to_db()  # same as doing it in another class
                    v.add_movie_to_db()
                    val = 'Baza pobrana!'
                except:
                    val = 'błąd pobierania bazy!'
            else:
                val = 'nieporawny kod'
                
        elif 'remove_all_videos' in request.POST:      
            if db_edit == 'remove':
                print('removing db ..')
                try:
                    movies = Movie.objects.all()
                    movies.delete()
                    val = 'baza usunięta'
                except:
                    val = 'nie udało się usunąć bazy'
            else:
                val = 'nieporawny kod'
    return render(request, 'editdb.html', {'form': form, 'val':val})



###################### get videos to db ######################

class Video_to_db():

    playlists = {
        'Szczepan Bentyn': 'UUcMCMdVFhU25uCpC4kJAo3A',
        'InPay Cryptokongres': 'PLg2mCY6UsYAd_1NeN3gjHxO2INNPuMmGk',
        'Cyfrowa ekonomia': 'UUgDd8b9KRigCXHiDOhfiwXw',
        'Phil Konieczny - recenzje kryptowalut': 'PL03G2FwOuZrwCdUdhiYJvWAIkoSezpEQs',
        'Phil Konieczny - krypto wiadomości': 'PL03G2FwOuZrzPLC3FXP1-29zNgy7QCQ-V',
        'DoradcaTV': 'PLTyhJimfcD0xMXbXsDZEwYJhBgf7_rWU5',
        'DoradcaTV - 7 zasad inwestowania': 'PLTyhJimfcD0xMXbXsDZEwYJhBgf7_rWU5',
        'DoradcaTV - wiedza o inwestowaniu': 'PLTyhJimfcD0wDiyIkPL8WKCk0w4zwt67Y',
        'Mike Satoshi - kraniki Kryptowalut': 'PLWqUcZHqsAutY0WtNzhXorTtprfZmT3Eb',
        'Mike Satoshi - kopanie Kryptowalut': 'PLWqUcZHqsAusm-oBqLof72s7GRfpT4mrp',
        'Mike Satoshi - scam alert': 'PLWqUcZHqsAutKOw962ogIDemma2-WF1h9',
        'Mike Satoshi - status raport': 'PLWqUcZHqsAusx0A7XgxcH9plHi4TnZBFV',
        'Mike Satoshi - kryptonewsy': 'PLWqUcZHqsAuumexQF9GIs-IvlNQe6ZJkS',
        'Mike Satoshi - kryptowaluty ogólnie': 'PLWqUcZHqsAusoHLwyAZGeSRhD8odnA63W',
        'Mike Satoshi - kryptowaluty dla początkujących': 'PLWqUcZHqsAuujnQ_VXKV-S9wH2en__19p',
        'Mateusz Szaton - portfele': 'PLQZ35aIAIIgeB1iFthdZnxuVpcd02-SoM',
        'Mateusz Szaton - krypto wiadomości': 'PLQZ35aIAIIgfOoPJtxexezz-DbFAVcqMc',
        'Mateusz Szaton - moje analizy': 'PLQZ35aIAIIgc7x5mTDytJL2YEqSL7qYVN',
        'Mateusz Szaton - kryptowaluty od podstaw': 'PLQZ35aIAIIger5l8J8jeUotYjofEwYvbn',  
        }

    playlists2 = {    
        'Kryptoraport': 'UUKy4pRGNqVvpI6HrO9lo3XA',
        'Kryptoraport1': 'PLQZ35aIAIIgeB1iFthdZnxuVpcd02-SoM',
        'Kryptoraport2': 'PLoW4zQupqVbOwpr4XPd_B6f2YO5w-k3Jc',
        'Kryptoraport3': 'PLoW4zQupqVbNXkXP8g7iNxueJubrzUVJX',
        }

    news_filter = [
        'Kryptoraport - wywiady',
        'Kryptoraport - rozmowa',
        'Kryptoraport - wywiady - mining',
        'Kryptoraport - co tam w NEM?',
        'Szczepan Bentyn - śniadanie z bitcoinem',
        'Szczepan Bentyn - wywiad',
        'Szczepan Bentyn - rozmowa',
        'Szczepan Bentyn - interview',
        'Mateusz Szaton - krypto wiadomości',
        'Mike Satoshi - kryptonewsy',
        'Mike Satoshi - kryptowaluty ogólnie',
        'Mike Satoshi - status raport',
        'Phil Konieczny - krypto wiadomości',
        'Cyfrowa ekonomia',
        'InPay Cryptokongres',
        'Kryptoraport - podsumowanie_tygodnia',
        'Kryptoraport - raporty',
        'Kryptoraport - podsumowanie_tygodnia',
    ]

    learn_filter = [
        'Kryptoraport - co tam w sieci?',
        'Kryptoraport - prawo a kryptowaluty',
        'Szczepan Bentyn - głupie pytania',
        'Szczepan Bentyn - kurs bitcoin',
        'Szczepan Bentyn - smart contracts',
        'Szczepan Bentyn - ICO',
        'Mateusz Szaton - moje analizy',
        'Mateusz Szaton - kryptowaluty od podstaw',
        'Mateusz Szaton - portfele',
        'Mike Satoshi - kryptowaluty dla początkujących',
        'Mike Satoshi - scam alert',
        'Mike Satoshi - kopanie Kryptowalut',
        'Mike Satoshi - kraniki Kryptowalut',
        'DoradcaTV - 7 zasad inwestowania',
        'DoradcaTV - wiedza o inwestowaniu',
        'Phil Konieczny - recenzje kryptowalut',
    ]

    nieposortowane = [
        'Kryptoraport - Tajniki kryptoświata',
    ]

    import apiclient
    import requests
    from apiclient.discovery import build
    from apiclient.errors import HttpError
    from oauth2client.tools import argparser

    DEVELOPER_KEY = 'AIzaSyAeKwWuoDQOZLsZkyJEMnu5ryxLLWV-vA0'
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    videoIDs = []
    videoInfo = {}
    all_videos = []

    def kryptoraport_get_sub_cat(self, video):
        title = video['title']
        sub_cat = video['sub_cat']
        if "sieci" in title.lower():
            sub_cat = 'Kryptoraport - co tam w sieci?'
        elif "podsumowanie" in title.lower():         
            if 'co tam ' not in title.lower():
                sub_cat = 'Kryptoraport - podsumowanie_tygodnia'
        elif "raport nr" in title.lower():  
            sub_cat = 'Kryptoraport - raporty'  
        elif "wywiad" in title.lower():
            sub_cat = 'Kryptoraport - wywiady'
        elif "rozmowa" in title.lower():
            sub_cat = 'Kryptoraport - rozmowa'
        elif "easy mine" in title.lower():  
            sub_cat = 'Kryptoraport - wywiady - mining'
        elif "w nem" in title.lower():  
            sub_cat = 'Kryptoraport - co tam w NEM?'   
        elif "co tam w sieci" in title.lower():  
            sub_cat = 'Kryptoraport - co tam w sieci?'
        elif "prawo a kryptowaluty" in title.lower():  
            sub_cat = 'Kryptoraport - prawo a kryptowaluty'   
        elif "tajniki kryptoświata" in title.lower():  
            sub_cat = 'Kryptoraport - Tajniki kryptoświata'  
        else:
            sub_cat = 'Kryptoraport - Nieposortowane'  
            
        
        return {'title': video['title'], 'sub_cat': sub_cat, 'videoID': video['videoID'], 'playlist_id': video['playlist_id']}

    def bentyn_get_sub_cat(self, video):
        title = video['title']
        sub_cat = video['sub_cat']

        if "śniadanie z bitcoinem" in title.lower():
            sub_cat = 'Szczepan Bentyn - śniadanie z bitcoinem'
        elif "wywiad" in title.lower():  
            sub_cat = 'Szczepan Bentyn - wywiad'    
        elif "rozmowa" in title.lower():  
            sub_cat = 'Szczepan Bentyn - rozmowa'
        elif "interview" in title.lower():  
            sub_cat = 'Szczepan Bentyn - interview'
        elif "głupię" in title.lower() or "głupie" in title.lower() or "gp" in title.lower():  
            sub_cat = 'Szczepan Bentyn - głupie pytania' 
        elif "kurs" in title.lower():  
            sub_cat = 'Szczepan Bentyn - kurs bitcoin' 
        elif "smartcontracts" in title.lower():  
            sub_cat = 'Szczepan Bentyn - smart contracts' 
        elif "ico" in title.lower():  
            sub_cat = 'Szczepan Bentyn - ICO' 
        else:
            sub_cat = 'Szczepan Bentyn - nieposortowane' 
        
        return {'title': video['title'], 'sub_cat': sub_cat, 'videoID': video['videoID'], 'playlist_id': video['playlist_id']}

    def get_youtube_playlist_videos(self, playlist_id, sub_cat) :
        playlistItem_request = self.youtube.playlistItems().list(
            part="snippet",
            playlistId=playlist_id,
            maxResults=50
        )

        while True :   
            playlistItems_result = playlistItem_request.execute()
            #print(playlistItems_result)

            for playlist_item in playlistItems_result["items"] :
                title = playlist_item["snippet"]["title"]
                videoID = playlist_item["snippet"]["resourceId"]["videoId"]
                #print ("%s (%s)" % (title, videoID))
                self.videoIDs.append(videoID)
                
                self.videoInfo[videoID] = dict(title=title,sub_cat=sub_cat,videoID=videoID,playlist_id=playlist_id)
                
                if sub_cat == 'kryptoraport':
                    self.videoInfo[videoID] = self.kryptoraport_get_sub_cat(self.videoInfo[videoID])
                elif sub_cat == 'Szczepan Bentyn':
                    self.videoInfo[videoID] = self.bentyn_get_sub_cat(self.videoInfo[videoID])
                
                self.all_videos.append(self.videoInfo[videoID])

            next_page = playlistItems_result.get("nextPageToken", "")
            if not next_page : 
                break

            playlistItem_request = self.youtube.playlistItems().list(
                part="snippet",
                playlistId=playlist_id,
                pageToken=next_page,
                maxResults=50
            )
        return self.videoInfo #, videoIDs 

    def get_all_videos(self):
        for sub_cat,playlist_id in Video_to_db.playlists.items():
            videos = self.get_youtube_playlist_videos(playlist_id,sub_cat)
            #all_videos.append(videos)
        for sub_cat,playlist_id in self.playlists2.items():
            videos = self.get_youtube_playlist_videos(playlist_id,'kryptoraport')
        return self.all_videos

    def get_youtube_video_info(self, videoid, sub_cat) :
        
        videoItem_request = self.youtube.videos().list(part='snippet,contentDetails,statistics',id=videoid)

        while True :   
            videoItem_result = videoItem_request.execute()
            #print(videoItem_result)

            for video_item in videoItem_result["items"] :
                #print('\n\n video_item',video_item)

                if sub_cat in self.news_filter:
                    icci_cat = 'news'
                elif sub_cat in self.learn_filter:
                    icci_cat = 'learn'
                else:
                    icci_cat = 'nieposortowane'

                try:
                    author = sub_cat.split(' -')[0]
                except:
                    author = ''
                
                try:
                    icci_sub_cat = sub_cat
                except:
                    icci_sub_cat = ''
                try:
                    title = video_item["snippet"]["title"]
                except:
                    title = ''
                try:
                    videoID = video_item["id"]
                except:
                    videoID = ''
                try:
                    publishedAt = video_item["snippet"]["publishedAt"]
                except:
                    publishedAt = ''
                try:
                    channelId = video_item["snippet"]["channelId"]
                except:
                    channelId = ''
                try:
                    description = video_item["snippet"]["description"]
                except:
                    description = ''
                try:
                    thumbnails_default = video_item["snippet"]["thumbnails"]['default']['url']
                except:
                    thumbnails_default = ''
                try:
                    thumbnails_medium = video_item["snippet"]["thumbnails"]['medium']['url']
                except:
                    thumbnails_medium = ''
                try:
                    thumbnails_high = video_item["snippet"]["thumbnails"]['high']['url']
                except:
                    thumbnails_high = ''
                try:
                    thumbnails_standard = video_item["snippet"]["thumbnails"]['standard']['url']
                except:
                    thumbnails_standard = ''
                try:
                    thumbnails_maxres = video_item["snippet"]["thumbnails"]['maxres']['url']
                except:
                    thumbnails_maxres = ''
                try:
                    tags = video_item["snippet"]["tags"]
                except:
                    tags = ''
                try:
                    categoryId = video_item["snippet"]["categoryId"]
                except:
                    categoryId = ''
                try:
                    liveBroadcastContent = video_item["snippet"]["liveBroadcastContent"]
                except:
                    liveBroadcastContent = ''
                try:
                    defaultLanguage = video_item["snippet"]["defaultLanguage"]
                except:
                    defaultLanguage = ''
                try:
                    duration = video_item["contentDetails"]['duration']
                except:
                    duration = ''
                try:
                    dimension = video_item["contentDetails"]['dimension']
                except:
                    dimension = ''
                try:
                    definition = video_item["contentDetails"]['definition']
                except:
                    definition = ''
                try:
                    caption = video_item["contentDetails"]['caption']
                except:
                    caption = ''
                try:
                    licensedContent = video_item["contentDetails"]['licensedContent']
                except:
                    licensedContent = False
                try:
                    projection = video_item["contentDetails"]['projection']
                except:
                    projection = ''
                try:
                    viewCount = video_item["statistics"]['viewCount']
                except:
                    viewCount = ''
                try:
                    likeCount = video_item["statistics"]['likeCount']
                except:
                    likeCount = ''
                try:
                    dislikeCount = video_item["statistics"]['dislikeCount']
                except:
                    dislikeCount = ''
                try:
                    favoriteCount = video_item["statistics"]['favoriteCount']
                except:
                    favoriteCount = ''
                try:
                    commentCount = video_item["statistics"]['commentCount']
                except:
                    commentCount = ''

                #print('videoid: ', videoid)
                video_full_info = {
                    'author': author,
                    'icci_cat': icci_cat,
                    'icci_sub_cat': icci_sub_cat,
                    'title': title,
                    'videoID' : videoID,
                    'publishedAt' : publishedAt,
                    'channelId'  : channelId,
                    'description' : description,
                    'thumbnails_default' : thumbnails_default,
                    'thumbnails_medium' : thumbnails_medium,
                    'thumbnails_high' : thumbnails_high,
                    'thumbnails_standard' : thumbnails_standard,
                    'thumbnails_maxres' : thumbnails_maxres,
                    'tags' : tags,
                    'categoryId' : categoryId,
                    'liveBroadcastContent' : liveBroadcastContent,
                    'defaultLanguage' : defaultLanguage,
                    'duration' : duration,
                    'dimension' : dimension,
                    'definition' : definition,
                    'caption' : caption,
                    'licensedContent' : licensedContent,
                    'projection' : projection,
                    'viewCount' : viewCount,
                    'likeCount' : likeCount,
                    'dislikeCount' : dislikeCount,
                    'favoriteCount' : favoriteCount,
                    'commentCount' : commentCount,
                }
                
            next_page = videoItem_result.get("nextPageToken", "")
            if not next_page : 
                break
        try: 
            return video_full_info
        except:
            video_full_info = {}
            return video_full_info


    def get_complete_video_info(self):
        video_full_info = []
        film = Movie()
        all_videos = self.get_all_videos()
        n=0
        for video in all_videos:
            n+=1
            print( n, video['videoID'])
            try:
                entry = Movie.objects.get(videoID=video['videoID'])
                print('\nJest W BAZE\n',entry)
            except:
                print('\nNIE MA W BAZE\n')
                if video['videoID'] not in video_full_info:
                    video_info = (self.get_youtube_video_info(videoid=video['videoID'], sub_cat=video['sub_cat']))
                    #print(video_info)
                    video_full_info.append(video_info)
                else:
                    print('jest w video_full_info')
        return video_full_info


    def add_movie_to_db(self):

        failed = []
        film = Movie()

        print('add_movie_to_db() w views.py')
        all_videos = self.get_complete_video_info()
        
        for v in all_videos:  
            print(v)
            try:          
                film.author = v['author']
            except:
                film.author = ''
            try:  
                film.icci_cat = v['icci_cat']
            except:
                film.icci_cat = ''
            try:  
                film.icci_sub_cat = v['icci_sub_cat'] 
            except:
                film.icci_sub_cat = ''
            try:
                film.title = v['title']
            except:
                film.title = ''
            try: 
                film.videoID = v['videoID']
            except:
                film.videoID = ''
            try: 
                film.publishedAt = v['publishedAt'] 
            except:
                film.publishedAt = None 
            try: 
                film.channelId = v['channelId']
            except:
                film.channelId = ''
            try: 
                film.description = v['description']
            except:
                film.description = ''
            try: 
                film.tags = v['tags']
            except:
                film.tags = ''
            try: 
                film.categoryId = v['categoryId'] 
            except:
                film.categoryId = ''
            try: 
                film.liveBroadcastContent = v['liveBroadcastContent'] 
            except:
                film.liveBroadcastContent = ''
            try: 
                film.defaultLanguage = v['defaultLanguage']
            except:
                film.defaultLanguage = ''
            try: 
                film.duration = v['duration']
            except:
                film.duration = ''
            try: 
                film.dimension = v['dimension']
            except:
                film.dimension = ''
            try: 
                film.definition = v['definition']
            except:
                film.definition = ''
            try: 
                film.caption = v['caption']
            except:
                film.caption = ''
            try: 
                film.licensedContent = v['licensedContent']
            except:
                film.licensedContent = ''
            try: 
                film.projection = v['projection']
            except:
                film.projection = ''
            try: 
                film.viewCount = v['viewCount']
            except:
                film.viewCount = ''
            try: 
                film.likeCount = v['likeCount']
            except:
                film.likeCount = ''
            try: 
                film.dislikeCount = v['dislikeCount']
            except:
                film.dislikeCount = ''
            try: 
                film.favoriteCount = v['favoriteCount']
            except:
                film.favoriteCount = ''
            try: 
                film.commentCount = v['commentCount']
            except:
                film.commentCount = ''
            try: 
                film.thumbnails_default = v['thumbnails_default']
            except:
                film.thumbnails_default = ''
            try: 
                film.thumbnails_medium = v['thumbnails_medium']
            except:
                film.thumbnails_medium = ''
            try: 
                film.thumbnails_high = v['thumbnails_high']
            except:
                film.thumbnails_high = ''
            try: 
                film.thumbnails_standard = v['thumbnails_standard']
            except:
                film.thumbnails_standard = ''
            try: 
                film.thumbnails_maxres = v['thumbnails_maxres']
            except:
                film.thumbnails_maxres = ''

            try:
                film.pk = None
                print(film.title)
                film.save()
            except:
                failed.append(v)
        
        #check for duplicates in db
        lastSeenId = float('-Inf')
        rows = Movie.objects.all().order_by('title')

        for row in rows:
            if row.title == lastSeenId:
                row.delete() # We've seen this id in a previous row
            else: # New id found, save it and check future rows for duplicates.
                lastSeenId = row.title 
            
        return 'baza zupdatowana'
                
        #template = loader.get_template('articles/index.html')
        #context = {
        #    'new_article_id': article.pk,
        #}
        #return HttpResponse(template.render(context, request))

