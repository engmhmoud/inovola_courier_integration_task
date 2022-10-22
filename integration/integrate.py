

from account.models import Courier
from base.models.base import Order
from base.serializer.OrderSerializer import OrderSerializerForCourier
from integration.helpers.call_api import call_courier_api
from integration.helpers.constants import ORDER_MODEL
from integration.shipbox.api import api_get_status_order as api_get_status_order_shipbox
from integration.shipbox.api import create_waybill as create_waybill_shipbox
from integration.shipbox.api import print_waybill as print_waybill_shipbox


def create_order(courier: Courier, instance: Order):
    order = OrderSerializerForCourier(instance)
    order.is_valid(raise_exception=True)
    if courier.name == Courier.SHIPOX_NAME_CHOICE:
        caller_data = create_waybill_shipbox(order.data)

    # ----- and others ...
    check, response = call_courier_api(**caller_data)

    if not check:
        raise Exception(response)


def print_waybill(order: Order):

    order.is_valid(raise_exception=True)
    if order.courier.name == Courier.SHIPOX_NAME_CHOICE:
        caller_data = print_waybill_shipbox(order_numbers=[order.order_number])

    # ----- and others ...
    check, response = call_courier_api(
        **caller_data, prepare_response=False, model=ORDER_MODEL)

    if not check:
        raise Exception(response)

    return check, response


def get_status(instance: Order):
    if instance.courier.name == Courier.SHIPOX_NAME_CHOICE:
        caller_data = api_get_status_order_shipbox(instance.order_number)
    # ----- and others ...

    return call_courier_api(**caller_data, model=ORDER_MODEL, courier=instance.courier)

    if not check:
        raise Exception(response)
