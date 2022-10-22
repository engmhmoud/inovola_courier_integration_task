# returned data structure api_link ,method,  header , body

from integration.shipbox.constants import API_LINK

method_post = 'post'
method_get = 'get'


def api_cancle_order(order_id):
    api_link = API_LINK(
    ) + f'customer/order/{order_id}/status?status=cancelled'
    return api_link, method_post, None, None


# we can define both web hooks in shipbox and get order status for shipbox and update it in db


def api_get_status_order(order_number):
    api_link = API_LINK() + f"customer/order/{order_number}/history_items"
    return api_link, method_get, None, None


def print_waybill(ids, order_numbers):
    ids_q = ""
    order_numbers_q = ""
    for idx, id in enumerate(ids):
        ids_q += f'{"" if idx ==0 else "&" }ids={id}'
    for idx, order_number in enumerate(order_numbers):
        order_numbers_q += f'{"" if idx ==0 else "&" }order_numbers={order_number}'

    api_link = API_LINK(
    ) + f'customer/orders/airwaybill_mini?{ids_q  if ids_q   else "" }{"," if ids_q and  order_numbers_q else "" }{order_numbers_q if order_numbers_q   else "" }'
    return api_link, method_get, None, None


def create_waybill(body):
    api_link = API_LINK() + f'customer/order'
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
            "passport_series": "AA",
            "passport_number": "12345678",
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
        "force_create": true,
        "agent": "Karim",
        "boxes": [
            {
            "description": "Big blue box",
            "height": 200,
            "length": 300,
            "line_items": [
                {
                "name": "Redmi note 8",
                "ean13_code": "8475624179572",
                "origin_country": "Uzbekistan",
                "price_per_unit": 10,
                "quantity": "10",
                "tax_code": "ZE0017",
                "desc": "Xiaomi mobile phones",
                "weight": 1
                }
            ],
            "weight": 1,
            "width": 300
            }
        ],
        "manifest": "EA202117",
        "placed_storage_address": "Tashkent, Mirzo-Ulugbek district, 100100"
    }
    """
    return api_link, method_post, None, body
