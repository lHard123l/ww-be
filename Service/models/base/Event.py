from django.db import models




class Event(models.Model):
    name                    =   models.CharField(max_length=50, null=False)
    short_description       =   models.CharField(max_length=100, default="")
    description             =   models.TextField(default="")
    start_time              =   models.DateTimeField(null=False)
    end_time                = models.DateTimeField(null=False)
    event_number            =   models.IntegerField(null=False)
    site_url                =   models.URLField(null=True)

