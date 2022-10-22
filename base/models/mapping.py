from codecs import unicode_escape_decode
from django.db import models

from account.models import Courier


class MapFeieldKey(models.Model):
    key_remote = models.CharField(max_length=255)
    key_local = models.CharField(max_length=255)
    map_object = models.ForeignKey("base.MapObject", on_delete=models.CASCADE)

    class Meta:
        unique_together = ("key_remote", "key_local", "map_object")


class MapValues(models.Model):
    key_value = models.CharField(max_length=255)
    key_remote = models.CharField(max_length=255)

    map_field = models.ForeignKey(
        "base.MapFeieldKey", on_delete=models.CASCADE)

    class Meta:
        unique_together = ("key_value", "key_remote", "map_field")

    # for example
    """
    map field :
    {   value : "en",
        map_field:{
            map_object:{
            model country local,
            model country remote,
            courier local              
        },
        key_local :country_code
        key_remote :country_code
        } 
    } """
    # mapping values like city code


class MapObject(models.Model):
    courier = models.ForeignKey("account.Courier", on_delete=models.CASCADE)
    model_local = models.CharField(max_length=255)  # name of model local
    model_remote = models.CharField(max_length=255)

    class Meta:
        unique_together = ("courier", "model_local", "model_remote")
