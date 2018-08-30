from django.db import models

# Create your models here.
class IcoEvent(models.Model):
    ico_title = models.CharField(max_length=500, default='',null=True, blank=True)
    ico_description = models.TextField(default="",null=True, blank=True)
    ico_img = models.CharField(max_length=128, default='',null=True, blank=True)
    ico_website_link = models.CharField(max_length=128, default='',null=True, blank=True)
    ico_start_time = models.DateTimeField(null=True, blank=True)
    ico_end_time = models.DateTimeField(null=True, blank=True)
    ico_icowatchlist_url = models.CharField(max_length=128, default='',null=True, blank=True)
    ico_source = models.CharField(max_length=128, default='',null=True, blank=True)
    ico_typ = models.CharField(max_length=10, default='',null=True, blank=True)
    

    def __str__(self):
        return self.name_with_year()

    def name_with_year(self):
        return str(self.ico_title) + " (" + str(self.ico_source) + ")"


class GetIco(models.Model):
    kod = models.CharField(max_length=128)