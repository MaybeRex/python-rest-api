from rest_framework import status

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'status': status.HTTP_200_OK
    }
