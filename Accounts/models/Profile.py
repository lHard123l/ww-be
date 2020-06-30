from django.db import models
from django_enum_choices.fields import EnumChoiceField
from Accounts.enums.UsersSex import Sex
from django.contrib.auth.models import User


class Profile(models.Model):

    name            =   models.CharField(null=True, max_length=30)
    surname         =   models.CharField(null=True, max_length=30)
    city            =   models.CharField(null=True, max_length=30)
    street          =   models.CharField(null=True, max_length=100)
    flat_number     =   models.CharField(null=True, max_length=10)
    postal_code     =   models.CharField(null=True, max_length=6)
    sex             =   EnumChoiceField(Sex)
    #image           =   models.ImageField(null=True)

    user            =   models.OneToOneField(User, on_delete=models.CASCADE)


    @property
    def is_filled(self):
        if self.name == None:
            return False
        if self.surname == None:
            return False
        if self.city == None:
            return False
        if self.street == None:
            return False
        if self.flat_number == None:
            return False
        if self.postal_code == None:
            return False
        return True

    objects         =   models.Manager()