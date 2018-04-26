from .models import Email
from django.http import JsonResponse, HttpResponse
from django.core.validators import validate_email, ValidationError

OK_RESP = {
    'ok': True,
    'data': {},
}

FAIL_RESP = {
    'ok': False,
    'reason': {
        'err': 40001,
        'desc': 'PARAM ERROR'
    },
}


def save_email(request, *args, **kwargs) -> JsonResponse:
    slug = request.GET.get('slug', '')
    email = request.GET.get('email', '')
    if not slug or not email:
        return JsonResponse(FAIL_RESP)
    try:
        validate_email(email)
    except ValidationError:
        return JsonResponse(FAIL_RESP)

    email_row, created = Email.objects.get_or_create(slug=slug, email=email)

    return JsonResponse(OK_RESP)


def ping(request, *args, **kwargs) -> HttpResponse:
    return HttpResponse('pong')
