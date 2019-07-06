# -*- coding: utf-8 -*-

"""Main module."""

import coloredlogs
from {{ cookiecutter.project_slug }}.logger import LoggingClass


class {{ cookiecutter.project_slug.title().replace('_', '').replace('-', '') }}(LoggingClass):
    def __init__(self, log_level="INFO"):

        self.logger.setLevel(log_level.upper())
        coloredlogs.install(level=log_level.upper())

    # Code goes here