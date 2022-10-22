
import requests

from base.models.mapping import MapFeieldKey, MapObject


def call_courier_api(url, method, header, body, expected_status_code=None, prepare_response=True, **kwargs):

    _response = requests.request(
        method=method, url=url, data=body, headers=header)

    if _response.status_code == expected_status_code if expected_status_code else str(_response.status_code).startswith('2'):
        return prepare_response_full(_response, True, **kwargs) if prepare_response else prepare_response_base(_response), True
    else:
        return prepare_response_full(_response, False, **kwargs)if prepare_response else prepare_response_base(_response), False

# from xml if xml to json only


def prepare_response_base(response):
    # step one for both successed and failed
    # 1 => # if xml
    # from xml to json

    # step2 for only success status
    # 2 => from json courier fields structure to our structure to make response readable if we need to display

    return response


def prepare_response_full(response, success, **kwargs):

    response = prepare_response_base(response=response)
    # step2

    data = response.data
    if success:
        model = kwargs.get('model', None)
        courier = kwargs.get('courier', None)
        if model and courier:
            map_obj = MapObject.objects.get(
                courier_id=courier, model_local=model)

            fields = MapFeieldKey.objects.filter(map_object=map_obj)

            result = {}
            for field in fields:

                result[field.key_local] = data.get(field.key_remote, None),

            return result

        if result:
            response.data = result

    return response
