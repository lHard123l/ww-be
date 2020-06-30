from rest_framework import serializers
from django_enum_choices.fields import EnumChoiceField
from Accounts.enums.UsersSex import Sex

class ProfileSerializer(serializers.Serializer):
    name            =   serializers.CharField(max_length=30, required=False)
    surname         =   serializers.CharField(max_length=30, required=False)
    city            =   serializers.CharField(max_length=30, required=False)
    street          =   serializers.CharField(max_length=100, required=False)
    flat_number     =   serializers.CharField(max_length=10, required=False)
    postal_code     =   serializers.CharField(max_length=6, required=False)
    sex             =   EnumChoiceField(Sex, null=True)



    def update(self, instance, validated_data):
        instance.name           =   validated_data.get('name', instance.name)
        instance.surname        = validated_data.get('surname', instance.surname)
        instance.city           = validated_data.get('city', instance.city)
        instance.street         = validated_data.get('street', instance.street)
        instance.flat_number    = validated_data.get('flat_number', instance.flat_number)
        instance.postal_code    = validated_data.get('postal_code', instance.postal_code)
        instance.sex            = validated_data.get('sex', instance.sex)
        instance.save()


    def is_valid(self, raise_exception=False, must_be_full_filled = False):
        if must_be_full_filled:
            if not (self.name and self.surname and self.city and self.street and self.flat_number and self.postal_code):
                return False
        return super().is_valid(raise_exception=raise_exception)
