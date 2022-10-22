
from django.urls import path

from base.views import ShipmentStatusView, WayBillView

urlpatterns = [
    path('create-waybill/', WayBillView.as_view()),
    path('print-waybill/', WayBillView.as_view()),
    path('shipment-status/<str:order_id>', ShipmentStatusView.as_view()),

]
