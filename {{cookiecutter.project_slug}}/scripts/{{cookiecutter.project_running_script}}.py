#!/usr/bin/env python3
{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
import argparse
{%- endif %}
import pathlib
import sys

from {{ cookiecutter.project_slug }}.{{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug.title().replace('_', '').replace('-', '') }}


def main():
    # Code goes here
    {%- if cookiecutter.command_line_interface|lower == 'argparse' %}
    parser = argparse.ArgumentParser(description="")

    parser.add_argument(
        "--loglevel",
        dest="log_level",
        default="INFO",
        help="log level to use, default [INFO], options [INFO, DEBUG, ERROR]",
    )
    args = vars(parser.parse_args())
    # Code goes here
    {%- endif %}

if __name__ == "__main__":
    main()
