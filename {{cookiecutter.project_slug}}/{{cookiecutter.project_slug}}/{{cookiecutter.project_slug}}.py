# -*- coding: utf-8 -*-

"""Main module."""


from loguru import logger

class {{ cookiecutter.project_slug.title().replace('_', '').replace('-', '') }}(LoggingClass):
    def __init__(self, log_level="INFO"):
        self.logger = logger
        self.logger.level(log_level.upper())

    # Code goes here