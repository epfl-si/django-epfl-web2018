from django import template
from django.contrib.messages import constants as message_constants
from django.template import Context
from django.template.loader import get_template

from django_epfl_web2018.core import get_web2018_setting

MESSAGE_LEVEL_CLASSES = {
    message_constants.DEBUG: "alert alert-warning",
    message_constants.INFO: "alert alert-info",
    message_constants.SUCCESS: "alert alert-success",
    message_constants.WARNING: "alert alert-warning",
    message_constants.ERROR: "alert alert-danger",
}

register = template.Library()


@register.filter
def web2018_message_classes(message):
    """Return CSS classes for a message based on its level and extra tags.

    This filter generates appropriate Bootstrap alert classes for Django
    messages based on the message level (DEBUG, INFO, SUCCESS, WARNING, ERROR)
    and any extra tags attached to the message.

    Args:
        message: A Django message object with attributes:
            - `level`: The message level (e.g., message_constants.INFO)
            - `extra_tags`: Additional CSS classes to include

    Returns:
        str: A space-separated string of CSS classes for the message.
             - Default: "alert alert-danger" if level is unknown
             - For known levels: "alert alert-{type}" where type is one of:
               - warning (DEBUG, WARNING)
               - info (INFO)
               - success (SUCCESS)
               - danger (ERROR)
             - Plus any extra_tags provided

    Example usage in template:
        <div class="{{ message|web2018_message_classes }}">
            {{ message }}
        </div>
    """
    classes = []

    extra_tags = getattr(message, "extra_tags", "")
    if extra_tags:
        classes.append(extra_tags)

    level = getattr(message, "level", None)
    if level in MESSAGE_LEVEL_CLASSES:
        classes.append(MESSAGE_LEVEL_CLASSES[level])
    else:
        classes.append("alert alert-danger")

    return " ".join(classes).strip()


@register.simple_tag(takes_context=True)
def web2018_messages(context, *args, **kwargs):
    """
    Render the web2018 messages template with the current context.

    This function ensures that Django messages are rendered using the
    web2018-specific messages template. It adds message constants
    to the context for use in templates and handles both Context
    objects and dictionaries.

    Args:
        context: The current template context, either a Context object
                 or a dictionary.
        *args: Additional positional arguments (ignored).
        **kwargs: Additional keyword arguments (ignored).

    Returns:
        str: The rendered HTML string of the messages template.

    Example usage in template:
        {% web2018_messages %}
    """
    if isinstance(context, Context):
        context = context.flatten()

    context["message_constants"] = message_constants

    template = get_template("web2018/messages.html")
    return template.render(context=context)


@register.simple_tag
def web2018_setting(name, default=None):
    """Return a value from the WEB2018 Django setting.

    This template tag reads the WEB2018 dictionary setting and returns
    the value for the given key. If the setting is undefined or
    malformed (not a Mapping), or the key is missing, the given default
    value is returned. Package-level DEFAULTS apply as the final
    fallback, so a value is only missing when the key is unknown to
    both the WEB2018 setting and the DEFAULTS configuration.

    Settings format (settings.py):
        WEB2018 = {"SHOW_BREADCRUMB": True}

    Args:
        name: The key to look up in the WEB2018 setting.
        default: The value returned when the key is missing from the
                 WEB2018 setting. None means that no value was given at
                 the call site and the package default applies.

    Returns:
        The value from the WEB2018 setting for the given key, the
        given default value or the package default.

    Example usage in template:
        {% web2018_setting 'SHOW_BREADCRUMB' True as show_breadcrumb %}
    """
    return get_web2018_setting(name, default)
