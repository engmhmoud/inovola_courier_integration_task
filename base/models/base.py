from django.db import models

from account.models import Sender

"""{
    "sender_data": {
        "address_type": "residential",
        "name": "Sherlock Holmes",
        "email": "mr.holmes@example.com",
        "apartment": "221",
        "building": "B",
        "street": "Baker Street",
        "city": {
          "code": "dubai"
        },
        "country": {
          "id": 229
        },
        "neighborhood": {
            "id":24876469,
            "name":"Al Quoz 1"
        },
        "phone": "+971541234567"
    },
    "recipient_data": {
        "address_type": "residential",
        "name": "Dr. Watson",
        "apartment": "221",
        "building": "B",
        "street": "Baker Street",
        "city": {
          "id": 4
        },
        "neighborhood": {
            "id":24876469,
            "name":"Al Quoz 1"
        },
        "phone": "+971543097580",
        "landmark": "Opposite to the Union Bus Station"
    },
    "dimensions": {
        "weight": 12,
        "width": 32,
        "length": 45,
        "height": 1,
        "unit": "METRIC",
        "domestic": true
    },
    "package_type": {
        "courier_type": "express_delivery"
    },
    "charge_items": [
        {
          "paid": false,
          "charge": 100,
          "charge_type": "cod"
        }
    ],
    "recipient_not_available": "do_not_deliver",
    "payment_type": "cash",
    "payer": "sender",
    "parcel_value": 100,
    "fragile": true,
    "note": "mobile phone",
    "piece_count": 1,
    "force_create": true
}
"""


class Order(models.Model):
    order_number = models.CharField(unique=True, max_length=255)
    courier = models.OneToOneField('account.courier')

    DO_NOT_DELIVER_CHOICE = "0"
    RECIPIENT_NOT_AVAILABLE_CHOICES = (
        (DO_NOT_DELIVER_CHOICE, "do_not_deliver"))
    CACH_CHOICE, ONLINE_PAYMENT = "0", "1"

    PAYMENT_TYPE = ((CACH_CHOICE, 'CACH_CHOICE',),
                    (ONLINE_PAYMENT, "ONLINE_PAYMENT"))

    dimension = models.OneToOneField('Dimension')
    domestic = models.BooleanField()
    fragile = models.BooleanField()

    recipient_not_available = models.CharField(
        choices=RECIPIENT_NOT_AVAILABLE_CHOICES, max_length=1)

    note = models.CharField(max_length=255)
    count = models.IntegerField()

    payment_type = models.CharField(choices=PAYMENT_TYPE, max_length=1)
    sender = models.ForeignKey("account.Sender")
    reciver = models.ForeignKey("account.Receiver")

    amount = models.IntegerField()
