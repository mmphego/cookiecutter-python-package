#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `{{ cookiecutter.project_slug }}` package."""

import unittest
import random
import warnings

from {{ cookiecutter.project_slug }}.{{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug.title().replace('_', '').replace('-', '') }}

class Test{{ cookiecutter.project_slug|title }}(unittest.TestCase):
    """Tests for `{{ cookiecutter.project_slug }}` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        raise NotImplementedError("method not implemented!")

    def tearDown(self):
        """Tear down test fixtures, if any."""
        raise NotImplementedError("method not implemented!")

    def test_000_something(self):
        """Test something."""
        raise NotImplementedError("method not implemented!")
