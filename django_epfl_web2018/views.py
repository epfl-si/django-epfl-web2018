from django.conf import settings
from django.shortcuts import render


def _render_error_page(request, status_code, template_base):
    language = getattr(request, "LANGUAGE_CODE", settings.LANGUAGE_CODE)
    template = f"{template_base}-{language}.html"

    try:
        return render(request, template, status=status_code)
    except Exception:
        fallback_template = f"{template_base}-en.html"
        return render(request, fallback_template, status=status_code)


def error_400(request, exception):
    return _render_error_page(request, 400, "web2018/includes/400")


def error_403(request, exception):
    return _render_error_page(request, 403, "web2018/includes/403")


def error_404(request, exception):
    return _render_error_page(request, 404, "web2018/includes/404")


def error_500(request):
    return _render_error_page(request, 500, "web2018/includes/500")
