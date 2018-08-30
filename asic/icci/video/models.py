from django.db import models

class ExtraInfo(models.Model):
    RODZAJE = {
        (0, 'Nieznany'),
        (1, 'Horror'),
        (2, 'Komedia'),
        (3, 'Sci-Fi'),
        (4, 'Drama')
    }
    czas_trwania = models.IntegerField(default=0)
    rodzaj = models.IntegerField(default=0, choices=RODZAJE)

class Movie(models.Model):
    author = models.CharField(max_length=128, default='',null=True, blank=True)
    icci_cat = models.CharField(max_length=128, default='',null=True, blank=True)
    icci_sub_cat = models.CharField(max_length=128, default='',null=True, blank=True)
    title = models.CharField(max_length=128, default='')
    videoID = models.CharField(max_length=128,  default='')
    publishedAt = models.DateTimeField(null=True, blank=True)
    channelId = models.CharField(max_length=128,  default='')
    description = models.TextField(default="",null=True, blank=True)
    tags = models.TextField(default="",null=True, blank=True)
    categoryId = models.CharField(max_length=128,  default='')
    liveBroadcastContent = models.CharField(max_length=128,  default='')
    defaultLanguage = models.CharField(max_length=128,  default='')
    duration = models.CharField(max_length=20,  default='')
    dimension = models.CharField(max_length=20,  default='')
    definition = models.CharField(max_length=10,  default='')
    caption = models.CharField(max_length=10,  default='')
    licensedContent = models.BooleanField(default='False')
    projection = models.CharField(max_length=20,  default='')
    viewCount = models.CharField(max_length=20,  default='')
    likeCount = models.CharField(max_length=20,  default='')
    dislikeCount = models.CharField(max_length=20,  default='')
    favoriteCount = models.CharField(max_length=20,  default='')
    commentCount = models.CharField(max_length=20,  default='')
    thumbnails_default = models.CharField(max_length=80,  default='')
    thumbnails_medium = models.CharField(max_length=80,  default='')
    thumbnails_high = models.CharField(max_length=80,  default='')
    thumbnails_standard = models.CharField(max_length=80,  default='')
    thumbnails_maxres = models.CharField(max_length=80,  default='')
   
    def __str__(self):
        return self.name_with_year()

    def name_with_year(self):
        return str(self.title) + " (" + str(self.author) + ")"

class GetMovies(models.Model):
    kod = models.CharField(max_length=128)
    