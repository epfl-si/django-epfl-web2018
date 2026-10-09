from django_epfl_web2018.core import get_web2018_settings


def web2018_settings(request):
    """Return the Web2018 settings for use in template contexts.

    This context processor exposes the Web2018 settings under the
    `web2018_settings` context variable so templates can read the
    configuration without a dedicated template tag per option.

    The package-level DEFAULTS configuration is baked into the exposed
    dictionary, so `{{ web2018_settings.SHOW_BREADCRUMB }}` works even
    when the WEB2018 setting is not defined. User values replace
    package defaults and, when the setting is malformed (not a
    Mapping), only the package defaults are exposed.

    Usage (settings.py):
        TEMPLATES = [
            {
                "OPTIONS": {
                    "context_processors": [
                        ...
                        "django_epfl_web2018.context_processors.web2018_settings",
                    ],
                },
            },
        ]

    Args:
        request: The current HTTP request (unused).

    Returns:
        dict: A dictionary with a single `web2018_settings` key holding
              the Web2018 settings merged with the package defaults.

    Example usage in template:
        {% if web2018_settings.SHOW_BREADCRUMB %}...{% endif %}
    """
    return {"web2018_settings": get_web2018_settings()}
