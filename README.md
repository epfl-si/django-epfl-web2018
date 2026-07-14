# django-epfl-web2018

[![Test Status][github-actions-image]][github-actions-url]
[![Coverage Status][codecov-image]][codecov-url]
[![PyPI version][pypi-image]][pypi-url]

Web2018 for Django.

## Requirements

- Python 3.8 or later
- Django 4.2, 5.2 or 6.0

## Installation

```bash
pip install django-epfl-web2018
```

## Documentation

### Settings

Add `django_epfl_web2018` to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
  ...
  "django_epfl_web2018",
  ...
]
```

### Routing

Edit your `urls.py` and add the following:

```python
handler400 = "django_epfl_web2018.views.error_400"
handler403 = "django_epfl_web2018.views.error_403"
handler404 = "django_epfl_web2018.views.error_404"
handler500 = "django_epfl_web2018.views.error_500"
```

### Base Template

> **File**: `templates/web2018/web2018.html`

This is the **master template** for all pages. It defines the overall
structure and layout.

### Available Template Blocks (Override Points)

- `web2018_title` → Page title.
- `web2018_extra_link` → Extra tags inside `<head>`.
- `web2018_app_name` → Application name.
- `web2018_header` → Custom header content (search, user menu, language).
- `web2018_breadcrumb_container` → Breadcrumb container.
- `web2018_breadcrumb` → Breadcrumb items.
- `web2018_nav_main` → Main navigation (mobile).
- `web2018_content` → Page content.
- `web2018_pre_footer` → Custom content that sits over/above the footer.
- `web2018_extra_js` → Extra tags just before `</body>`.

[github-actions-image]: https://github.com/epfl-si/django-epfl-web2018/actions/workflows/test.yml/badge.svg?branch=main
[github-actions-url]: https://github.com/epfl-si/django-epfl-web2018/actions/workflows/test.yml
[codecov-image]: https://codecov.io/gh/epfl-si/django-epfl-web2018/graph/badge.svg?token=484E6QJKKJ
[codecov-url]: https://codecov.io/gh/epfl-si/django-epfl-web2018
[pypi-image]: https://img.shields.io/pypi/v/django-epfl-web2018
[pypi-url]: https://pypi.org/project/django-epfl-web2018/
