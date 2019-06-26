{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}

{% for _ in cookiecutter.project_name %}={% endfor %}
    {{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{% if is_open_source %}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg?color=green&label=pypi%20release
    :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}

.. image:: https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg
        :target: https://travis-ci.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}

.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest
        :target: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status
{%- endif %}

{% if cookiecutter.add_python_version_badge == 'y' %}
.. image:: https://img.shields.io/badge/Python-3.6%2B-red.svg
        :target: https://www.python.org/downloads/
{% endif %}

{% if cookiecutter.add_python_version_badge == 'y' %}
.. image:: https://img.shields.io/github/license/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg
        :target: LICENCE
{% endif %}


{% if cookiecutter.add_saythanks_badge == 'y' %}
.. image: https://img.shields.io/badge/say-thanks-ff69b4.svg
    :target: https://saythanks.io/to/{{ cookiecutter.github_username }}
{% endif %}


{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
* Documentation: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io.
{% endif %}

Installation
--------

* TODO


Usage
--------

* TODO

Oh, Thanks!
-------

By the way... Click if you'd like to [say thanks](https://saythanks.io/to/{{ cookiecutter.github_username}})... :) else *Star* it.

✨🍰✨


Feedback
-------

Feel free to fork it or send me PR to improve it.


Credits
-------

This package was created with Cookiecutter_ and the `mmphego/cookiecutter-python-package`_ project template.

.. _`mmphego/cookiecutter-python-package`: https://github.com/mmphego/cookiecutter-python-package

