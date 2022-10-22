

from rest_framework import serializers

from base.models.base import Order
from base.models.mapping import MapFeieldKey, MapObject


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"


class OrderSerializerForCourier(OrderSerializer):
    def to_representation(self, instance):
        map = MapObject.objects.get(
            pk=self.context.get('courier'), model_local='Order')

        map_fields = MapFeieldKey.objects.filter(map_object=map).all()
        result = {}
        for field in map_fields:

            result[field.key_remote] = getattr(instance, field.key_local)

        return result
