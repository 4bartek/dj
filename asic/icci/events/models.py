from django.db import models

# Create your models here.
class Event(models.Model):
    event_title = models.CharField(max_length=128, default='',null=True, blank=True)
    coins_id = models.CharField(max_length=28, default='',null=True, blank=True)
    coins_name = models.CharField(max_length=128, default='',null=True, blank=True)
    coins_symbol = models.CharField(max_length=28, default='',null=True, blank=True)
    event_description = models.TextField(default="",null=True, blank=True)
    event_proof = models.CharField(max_length=128, default='',null=True, blank=True)
    event_source = models.CharField(max_length=128, default='',null=True, blank=True)
    event_date = models.DateTimeField(null=True, blank=True)
    event_created_date = models.DateTimeField(null=True, blank=True)
    event_feed_source = models.CharField(max_length=40, default='',null=True, blank=True)
    event_is_hot = models.BooleanField(default='False')
    event_vote_count = models.CharField(max_length=12, default='',null=True, blank=True)
    event_positive_vote_count = models.CharField(max_length=12, default='',null=True, blank=True)
    event_percentage = models.CharField(max_length=5, default='',null=True, blank=True)
    event_event_cat_id = models.CharField(max_length=12, default='',null=True, blank=True)
    event_event_cat_name = models.CharField(max_length=128, default='',null=True, blank=True)
    event_tip_symbol = models.CharField(max_length=12, default='',null=True, blank=True)
    event_tip_adress = models.CharField(max_length=128, default='',null=True, blank=True)
    event_twitter_account = models.CharField(max_length=128, default='',null=True, blank=True)

    def __str__(self):
        return self.name_with_year()

    def name_with_year(self):
        return str(self.event_title)


class GetEvents(models.Model):
    kod = models.CharField(max_length=128)