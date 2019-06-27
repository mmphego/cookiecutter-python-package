#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""The setup script."""

import io
import os
import sys
from shutil import rmtree

from setuptools import Command, find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

# Package meta-data.
AUTHOR = "{{ cookiecutter.full_name.replace('\"', '\\\"') }}"
DESCRIPTION = "{{ cookiecutter.project_short_description }}"
EMAIL = "{{ cookiecutter.email }}"
NAME = "{{ cookiecutter.project_slug }}"
REQUIRED = [
    # put all required packages here
    "black", "coverage", "flake8", "isort",
    "pip", "pytest", "tox", "twine", "wheel",
]

REQUIRES_PYTHON = ">=3.6.0"
URL = "https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}"
VERSION = "{{ cookiecutter.version }}"


try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

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

        self.status("Uploading the package to PyPI via Twine...")
        os.system("twine upload dist/*")

        self.status("Pushing git tags...")
        os.system(f"git tag v{about["__version__"]}")
        os.system("git push --tags")

        sys.exit()


setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
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
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=['pytest', 'unittest'],
    project_urls={
        "Bug Reports": f"{URL}/issues",
        "Source": URL,
        "Say Thanks!": f"https://saythanks.io/to/{{ cookiecutter.github_username }}",
    },
    zip_safe=False,
    # $ setup.py publish support.
    cmdclass={"upload": UploadCommand},
)
