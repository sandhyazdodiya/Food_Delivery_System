from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from django.db import IntegrityError
from .utils import custom_exception_handler 

def get_json(status, response_type, headers, message, serializer=None):
    if serializer is None:
        response_data = {'status_code': status, 'type': response_type, 'headers': headers, 'message': message}
    else:
        response_data = {'status_code': status, 'type': response_type, 'data': serializer.data, 'headers': headers,
                         'message': message}
    return response_data

class ViewSetPatch(object):
    def create(self, request, *args, **kwargs):
        try:
            serializer = super().create(request, *args, **kwargs)
            print(serializer.data)
            response_data = get_json(HTTP_200_OK, '+OK', 'Success', 'Created Successfully', serializer)
            return Response(response_data)
        except IntegrityError as exc:
            raise custom_exception_handler(exc, request)

    def list(self, request, *args, **kwargs):
        try:
            serializer = super().list(request, *args, **kwargs)
            response_data = get_json(HTTP_200_OK, '+OK', 'Success', 'Listed Successfully', serializer)
            return Response(response_data)
        except IntegrityError as exc:
            raise custom_exception_handler(exc, request)

    def retrieve(self, request, *args, **kwargs):
        try:
            serializer = super().retrieve(request, *args, **kwargs)
            response_data = get_json(HTTP_200_OK, '+OK', 'Success', 'Retrieved Successfully', serializer)
            return Response(response_data)
        except IntegrityError as exc:
            raise custom_exception_handler(exc, request)

    def update(self, request, *args, **kwargs):
        try:
            serializer = super().update(request, *args, **kwargs)
            response_data = get_json(HTTP_200_OK, '+OK', 'Success', 'Updated Successfully', serializer)
            return Response(response_data)
        except IntegrityError as exc:
            raise custom_exception_handler(exc, request)

    def destroy(self, request, *args, **kwargs):
        try:
            serializer = super().destroy(request, *args, **kwargs)
            response_data = get_json(HTTP_200_OK, '+OK', 'Success', 'Destroyed Successfully', serializer)
            return Response(response_data)
        except IntegrityError as exc:
            raise custom_exception_handler(exc, request)