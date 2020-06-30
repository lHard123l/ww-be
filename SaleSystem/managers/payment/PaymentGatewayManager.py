import hashlib
import json
import requests
from django.db import models



class PaymentGatewayManager(models.Manager):
    def make_request(self, url, data):
        response = requests.post(url, data=data)
        if response.status_code == 200:
            return None

        return response.json()

    def count_checksum(self, merchantId, posId, ):
        sha_384 = hashlib.sha384()
        sha_384.update(json.dumps(json_data))
        return sha_384.hexdigest()