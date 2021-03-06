{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
# {{ cookiecutter.project_name }}

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![GitHub](https://img.shields.io/github/license/{{ cookiecutter.github_username}}/{{ cookiecutter.project_slug }}.svg)](LICENSE)
[![Build Status](https://img.shields.io/travis/{{ cookiecutter.github_username}}/{{ cookiecutter.project_slug }}.svg)](https://travis-ci.com/{{ cookiecutter.github_username}}/{{ cookiecutter.project_slug }})
{% if cookiecutter.add_coveralls_badge == 'y' %}
[![Coverage Status](https://coveralls.io/repos/github/{{ cookiecutter.github_username}}/{{ cookiecutter.project_slug }}/badge.svg?branch=master)](https://coveralls.io/github/{{ cookiecutter.github_username}}/{{ cookiecutter.project_slug }}?branch=master)
{% endif %}
{% if cookiecutter.add_codacy_badge == 'y' %}
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/43713e0b78f547e8912ff05c9350cffb)](https://app.codacy.com/app/{{ cookiecutter.github_username}}/{{ cookiecutter.project_slug }}?utm_source=github.com&utm_medium=referral&utm_content={{ cookiecutter.github_username}}/{{ cookiecutter.project_slug }}&utm_campaign=Badge_Grade_Dashboard)
{% endif %}
{% if cookiecutter.add_python_version_badge == 'y' %}
[![Python](https://img.shields.io/badge/Python-3.6%2B-red.svg)](https://www.python.org/downloads/)
{% endif %}
{% if cookiecutter.add_pypi_badge == 'y' %}
![PyPI](https://img.shields.io/pypi/v/{{cookiecutter.project_slug }}.svg?color=green&label=pypi%20release)
![PyPI - Downloads](https://img.shields.io/pypi/dm/{{cookiecutter.project_slug }}.svg?label=PyPi%20Downloads)
{% endif %}
{% if cookiecutter.add_saythanks_badge == 'y' %}
[![saythanks](https://img.shields.io/badge/say-thanks-ff69b4.svg)](https://saythanks.io/to/{{ cookiecutter.github_username }})
{% endif %}
{% if cookiecutter.add_donate_badge == 'y' %}
[![Donate](https://img.shields.io/badge/Donate-%24-green.svg)](https://paypal.me/{{ cookiecutter.paypal_username }})
{% endif %}

{{ cookiecutter.project_short_description }}

# Installation

To install {{ cookiecutter.project_name }}, run this command in your terminal:

```python
    pip install git+https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git
    
```

This is the preferred method to install {{ cookiecutter.project_name }},
as it will always install the most recent stable release.

If you don't have [pip](https://pip.pypa.io) installed,
this [Python installation guide](http://docs.python-guide.org/en/latest/starting/installation/) can guide you through the process.

## From sources

The sources for {{ cookiecutter.project_name }} can be downloaded from the [Github repo](https://github.com/{{ cookiecutter.github_username}}/{{ cookiecutter.project_slug }}).

You can either clone the public repository:

```bash
git clone git://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
```

Or download the [tarball](https://github.com/{{ cookiecutter.github_username}}/{{ cookiecutter.project_slug }}/tarball/master):

```bash
curl  -OL https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/tarball/master
```

Once you have a copy of the source, you can install it with:

```bash
python setup.py install
```

# Usage

```bash
{{cookiecutter.project_running_script}}.py -h
```

or

```bash
docker build -t "$USER/$(basename $PWD)" .
docker run --rm -ti --volume "$PWD":/app "$USER/$(basename $PWD)" \
    {{cookiecutter.project_running_script}}.py -h
```

# Donations

If you like this and want to buy me a cup of coffee, please click the donation button above or click this [link](https://paypal.me/{{ cookiecutter.paypal_username }}) ☕

# Feedback

Feel free to fork it or send me PR to improve it.

# Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [mmphego/cookiecutter-python-package](https://github.com/mmphego/cookiecutter-python-package) project template.
