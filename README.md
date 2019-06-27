# Cookiecutter Python Package

[![Updates](https://pyup.io/repos/github/mmphego/cookiecutter-python-package/shield.svg)](https://pyup.io/repos/github/mmphego/cookiecutter-python-package/)

[![image](https://travis-ci.com/mmphego/cookiecutter-python-package.svg?branch=master)](https://travis-ci.com/mmphego/cookiecutter-python-package)

-   GitHub repo: <https://github.com/mmphego/cookiecutter-python-package/>

# Features

-   Testing setup with `unittest` and `python setup.py test` or
    `py.test`
-   [Travis-CI](http://travis-ci.org/): Ready for Travis Continuous
    Integration testing

# Build Status

[![Linux build status on Travis CI](https://img.shields.io/travis/mmphego/cookiecutter-python-package.svg)](https://travis-ci.org/mmphego/cookiecutter-python-package)

# Quickstart

Install the latest Cookiecutter if you haven't installed it yet (this requires Cookiecutter 1.4.0 or higher):
```bash
pip install -U cookiecutter
```

Generate a Python package project:

```bash
cookiecutter https://github.com/mmphego/cookiecutter-python-package.git
```

Then:

-   Create a repo and put it there.
-   Add the repo to your [Travis-CI](http://travis-ci.org/) account.
-   Install the requirements into a virtualenv.
    (`pip install -r requirements.txt`)
-   [Register](https://packaging.python.org/distributing/#register-your-project)
    your project with PyPI.
-   Release your package by pushing a new tag to master.
<!-- -   Activate your project on [pyup.io](https://pyup.io/). -->

For more details, see the [cookiecutter-pypackage
tutorial](https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html).


### Fork This / Create Your Own

If you have differences in your preferred setup, I encourage you to fork
this to create your own version. Or create your own; it doesn't strictly
have to be a fork.

-   Once you have your own version working, add it to the Similar
    Cookiecutter Templates list above with a brief description.
-   It's up to you whether or not to rename your fork/own version. Do
    whatever you think sounds good.

### Or Submit a Pull Request

I also accept pull requests on this, if they're small, atomic, and if
they make my own packaging experience better.

# Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter)