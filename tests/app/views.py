from django.core.exceptions import BadRequest, PermissionDenied


def error_400(request):
    raise BadRequest("Bad request: invalid data.")


def error_403(request):
    raise PermissionDenied("You are not allowed to access this.")


def error_500(request):
    raise Exception("This is a 500 error")
