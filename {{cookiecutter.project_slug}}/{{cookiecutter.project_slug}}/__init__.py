# -*- coding: utf-8 -*-

"""Top-level package for {{ cookiecutter.project_name }}."""

__author__ = """{{ cookiecutter.full_name }}"""
__email__ = '{{ cookiecutter.email }}'

# Python standard library
import os
import pkgutil

from {{ cookiecutter.project_slug }} import __version__

__version__ = __version__.__version__

__all__ = [module for _, module, _ in pkgutil.iter_modules([os.path.dirname(__file__)])]
