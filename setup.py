import os
import sys
from setuptools import setup


PACKAGE = "pytest-allure-adaptor"
VERSION = "1.6.7"


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def main():
    setup(
        name=PACKAGE,
        version=VERSION,
        description=("Plugin for py.test to generate allure xml reports"),
        author="pupssman",
        author_email="pupssman@yandex-team.ru",
        packages=["allure"],
        url="https://github.com/allure-framework/allure-python",
        long_description=read('README.rst'),
        entry_points={'pytest11': ['allure_adaptor = allure.pytest_plugin']},
        install_requires=[
            "lxml>=3.2.0",
            "pytest>=2.7.0",
            "namedlist",
            "six>=1.9.0"] +
            ["enum34"] if sys.version < "3.4" else []
    )

if __name__ == '__main__':
    main()
