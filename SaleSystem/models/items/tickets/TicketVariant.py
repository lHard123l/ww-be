from django.db import models
from Service.models import Image



class TicketVariant(models.Model):
    name                =   models.CharField(max_length=20)
    event               =   models.ForeignKey(Event, on_delete=models.CASCADE)
    short_description   =   models.CharField(max_length=100)
    description         =   models.CharField(max_length=500)
    main_image          =   models.OneToOneField(Image, on_delete=models.CASCADE)
    minimal_price       =   models.IntegerField()
