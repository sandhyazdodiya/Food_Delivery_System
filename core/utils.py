from rest_framework.views import exception_handler
from rest_framework.response import Response
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import exceptions, status


def success_response(message, data=None, url=None):
    response = {"message": message, "type": "+OK", "status_code": status.HTTP_200_OK, "headers": "Success"}
    if data:
        response["data"] = data
    if url:
        response["url"] = url
    return Response(response, status=status.HTTP_200_OK)


def error_response(message, errors=None, status_code=status.HTTP_202_ACCEPTED):
    response = {"message": message, "status_code": status_code, "type": "-ERR"}
    if errors:
        response["errors"] = errors
    return Response(response, status=status_code)






def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    if isinstance(exc, (exceptions.AuthenticationFailed, exceptions.NotAuthenticated)):
        response.status_code = status.HTTP_401_UNAUTHORIZED

    # Now add the HTTP status code to the response.
    if response is not None:
        data = response.data
        errors = {}
        for field, value in data.items():
            if isinstance(value, dict):
                for k, v in value.items():
                    errors[k] = v[0] if isinstance(v, list) else v
                continue
            errors[field] = value[0] if isinstance(value, list) else value
        response.data = {'errors': errors, "type": '-ERR', 'status_code': response.status_code}
    return response


# def server_error(request, *args, **kwargs):
#     """
#     If the DEBUG is True, this method will handle the internal server error,
#     And response the json id the request if ajax request else render the page with error msg.
#     """
    
#     if request.is_ajax():
#         data = {'errors': {'detail': 'Internal Server Error, Please try again later'}}
#         return JsonResponse(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#     else:
#         return render(request, "error500.html", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
