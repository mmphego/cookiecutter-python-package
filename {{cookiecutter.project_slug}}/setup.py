#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""The setup script."""

import io
import os
import sys

from subprocess import Popen
from shutil import rmtree

from setuptools import Command, find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

# Package meta-data.
AUTHOR = "{{ cookiecutter.full_name.replace('\"', '\\\"') }}"
DESCRIPTION = "{{ cookiecutter.project_short_description }}"
EMAIL = "{{ cookiecutter.email }}"
NAME = "{{ cookiecutter.project_slug }}"
REQUIRED = [
    "loguru",
]

EXTRAS = {
    'dev' :["twine", "black", "flake8", "isort", "pip", "twine", "wheel"],
    'testing': ["coverage", "pytest", "tox"]
}

REQUIRES_PYTHON = ">=3.6.0"
URL = "https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}"
VERSION = "{{ cookiecutter.version }}"


try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        LONG_DESCRIPTION = "\n" + f.read()
except FileNotFoundError:
    LONG_DESCRIPTION = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, "__version__.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION

SCRIPTS = []
for dirname, dirnames, filenames in os.walk("scripts"):
    for filename in filenames:
        SCRIPTS.append(os.path.join(dirname, filename))

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}


class UploadCommand(Command):
    """Support setup.py upload."""

    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print(f"\033[1m{s}\033[0m")

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(here, "dist"))
        except OSError:
            pass

        try:
            import twine
        except ImportError:
            errmsg = "\n'Twine' is not installed.\n\nRun: \n\tpip install twine"
            self.status(errmsg)
            raise SystemExit(1)

        self.status("Building Source and Wheel (universal) distribution...")
        os.system(f"{sys.executable} setup.py sdist bdist_wheel --universal")
        try:
            cmd = "twine test dist/*".split(" ")
            p = Popen(cmd, bufsize=-1)
            p.communicate()
            assert p.returncode == 0
        except AssertionError:
            self.status("Failed Twine Test.")
            raise

        try:
            self.status("Uploading the package to PyPI via Twine...")
            cmd = "twine upload dist/*".split()
            p = Popen(cmd, bufsize=-1)
            p.communicate()
        except AssertionError:
            self.status("Failed to upload to PyPi.")
            raise
        else:
            self.status("Pushing git tags...")
            os.system(f"git tag v{about.get('__version__')}")
            os.system("git push --tags")
            response = input("Do you want to generate a CHANGELOG.md? (y/n) ")
            if response.lower() == 'y':
                self.status("Generating the CHANGELOG.md.")
                os.system("make changelog")
            sys.exit(p.returncode)


setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author=NAME,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(
        include=['{{ cookiecutter.project_slug }}'],
        exclude=["tests", "*.tests", "*.tests.*", "tests.*"]
        ),
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    scripts=SCRIPTS,
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    classifiers=[
        'Intended Audience :: Developers',
{%- if cookiecutter.open_source_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.open_source_license] }}',
{%- endif %}
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='{{ cookiecutter.project_slug }}',
    test_suite='tests',
    tests_require=['pytest', 'unittest'],
    project_urls={
        "Bug Reports": f"{URL}/issues",
        "Source": URL,
        "Say Thanks!": f"https://saythanks.io/to/{{ cookiecutter.github_username }}",
        "Donate!": f"https://paypal.me/{{ cookiecutter.paypal_username }}",
    },
    zip_safe=False,
    # $ setup.py publish support.
    cmdclass={"upload": UploadCommand},
)
