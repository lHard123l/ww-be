from django.db import models
from django.utils.timezone import datetime
# Create your models here.



class Player(models.Model):
    name                =   models.CharField(max_length=100, null=True)
    url                 =   models.URLField(default=None)
    api_key             =   models.CharField(max_length=500, null=True)
    activation_time     =   models.DateTimeField(null=True)
    expiration_time     =   models.DateTimeField(null=True)


    @property
    def is_active(self):
        if self.url == None:
            return False
        if self.api_key == None:
            return False
        if self.activation_time > datetime.now():
            return False
        if self.expiration_time < datetime.now():
            return False
        return True
