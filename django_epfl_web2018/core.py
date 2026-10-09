from collections.abc import Mapping

from django.conf import settings

DEFAULTS = {"SHOW_BREADCRUMB": True, "SITE_TITLE_SUFFIX": "EPFL"}


def _user_settings():
    """Return the WEB2018 Django setting when it is a Mapping.

    Returns:
        dict: The WEB2018 Django setting or an empty dictionary when
              it is not defined or is malformed.
    """
    web2018_settings = getattr(settings, "WEB2018", None)
    if not isinstance(web2018_settings, Mapping):
        return {}
    return web2018_settings


def get_web2018_setting(name, default=None):
    """Return a value from the WEB2018 Django setting.

    The value is resolved with the following precedence:

    1. The value from the WEB2018 Django setting when the key is
       present.
    2. The given `default` argument when it is not None. None is the
       sentinel meaning that no value was given at the call site.
    3. The value from the package-level DEFAULTS configuration.

    Args:
        name: The key to look up in the WEB2018 setting.
        default: The value returned when the key is missing from the
                 WEB2018 setting. None means that no value was given at
                 the call site and the package default applies.

    Returns:
        The value from the WEB2018 setting for the given key, the
        given default value or the package default.

    Example:
        from django_epfl_web2018.core import get_web2018_setting

        get_web2018_setting("SHOW_BREADCRUMB")
    """
    user_settings = _user_settings()
    if name in user_settings:
        return user_settings[name]
    if default is not None:
        return default
    return DEFAULTS.get(name)


def get_web2018_settings():
    """Return the Web2018 settings merged with the package defaults.

    The WEB2018 Django setting is shallow-merged over the package-level
    DEFAULTS configuration, meaning that user values replace package
    defaults. When the setting is not defined or is malformed (not a
    Mapping), only the package defaults are returned.

    Returns:
        dict: The merged Web2018 settings.
    """
    return {**DEFAULTS, **_user_settings()}
