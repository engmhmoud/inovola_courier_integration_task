from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from account.models import Courier
from base.models.base import Order
from base.serializer.OrderSerializer import OrderSerializer, OrderSerializerForCourier
from integration.integrate import get_status, print_waybill
# Create your views here.


class APIViewBase(APIView):
    model = None

    def get_object(self, pk=None, **kwargs):
        model = kwargs.get('model', self.model)
        try:
            return model.objects.get(pk=pk, **kwargs)
        except:
            raise Http404


class WayBillView(APIViewBase):
    model = Order
    serializer = OrderSerializer
    serializer_for_courier = OrderSerializerForCourier

    def post(self, request):
        courier_id = request.data.get('courier_id')
        courier = self.get_object(model=Courier, pk=courier_id)
        serializer = self.serializer(data=request.data, context={
                                     'courier': courier_id})
        if serializer.is_valid():
            serializer.save(courier=courier)
        return Response()

    def get(self, request, pk):
        order = self.get_object(pk=pk)

        check, res = print_waybill(order)

        return Response(res.data, status=status.HTTP_200_OK if check else status.HTTP_400_BAD_REQUEST)


class ShipmentStatusView(APIViewBase):
    model = Order
    serializer = OrderSerializer

    def get(self, request, order_id):
        order = self.get_object(order_id)
        check, response = get_status(order)
        if not check:
            return Response(response)

        ser = self.serializer(instance=order, data=response.data, partial=True)

        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
