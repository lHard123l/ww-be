from rest_framework import serializers

from SaleSystem.models.payment.Przelewy24 import Przelewy24


class Przelewy24Serializer(serializers.Serializer):
    ### REQUIRED FIELDS ###
    merchant_id         = serializers.CharField(max_length=50, required=True)
    pos_id              = serializers.CharField(max_length=50, required=True)
    session_id          = serializers.CharField(max_length=50, required=True)
    amount              = serializers.FloatField(required=True)
    currency            = serializers.CharField(max_length=3, required=True)
    description         = serializers.CharField(max_length=1000, required=True)
    email               = serializers.EmailField(required=True)

    country             = serializers.CharField(max_length=2, required=True)
    language            = serializers.CharField(max_length=2, required=True)

    url_return          = serializers.CharField(max_length=250, required=True)
    sign                = serializers.CharField(max_length=100, required=True)

    client_name         = serializers.CharField(max_length=50, required=True)

    ### ADDITIONAL FIELDS ###

    address             =   serializers.CharField(max_length=80)
    postal_code         =   serializers.CharField(max_length=10)
    city                =   serializers.CharField(max_length=50)
    phone_number        =   serializers.IntegerField()
    method              =   serializers.IntegerField()
    url_status          =   serializers.CharField(max_length=250)
    timeLimit           =   serializers.IntegerField(max_length=2, default=0)
    channel             =   serializers.IntegerField()
    shipping_cost       =   serializers.FloatField()
    transfer_label      =   serializers.CharField(max_length=20)
    mobile_lib          =   serializers.IntegerField()
    sdk_version         =   serializers.CharField(max_length=10)
    encoding            =   serializers.CharField(max_length=15)
    method_ref_id       =   serializers.CharField(max_length=250)

    
    def is_valid(self, raise_exception=False):
        pass

    def create(self, validated_data, context):

        return Przelewy24(**validated_data)

