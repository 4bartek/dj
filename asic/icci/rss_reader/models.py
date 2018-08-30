from django.db import models

# Create your models here.

class Feeds(models.Model):
    rss_feed_title = models.CharField(max_length=500, default='',null=True, blank=True)
    rss_feed_description = models.TextField(default="",null=True, blank=True)
    rss_feed_img = models.CharField(max_length=128, default='',null=True, blank=True)
    rss_feed_link = models.CharField(max_length=128, default='',null=True, blank=True)
    rss_feed_published = models.DateTimeField(null=True, blank=True)
    rss_feed_source = models.CharField(max_length=128, default='',null=True, blank=True)
    def __str__(self):
        return self.name_with_year()

    def name_with_year(self):
        return str(self.rss_feed_title) + " (" + str(self.rss_feed_description) + ")"


class GetFeeds(models.Model):
    kod = models.CharField(max_length=128)