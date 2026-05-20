from django import template
from django.contrib.messages import constants as message_constants
from django.template import Context
from django.template.loader import get_template

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
