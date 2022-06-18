#!/usr/bin/env python

import os

from setuptools import find_packages, setup

here = os.path.dirname(os.path.abspath(__file__))
f = open(os.path.join(here, 'README.md'))
long_description = f.read().strip()
f.close()


setup(
    name='fastapi_migrate',
    version="1.0.0",
    author='Thomas Saied',
    author_email="thomas.adel31@gmail.com",
    url='https://github.com/thomas545/fastapi_migrate',
    description='FastAPI Migrations is an extension that handles SQLAlchemy database migrations for FastAPI applications using Alembic.',
    license='GNU',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='fastapi migrate fastapi_migrations alembic sqlalchemy',
    zip_safe=False,
    install_requires=[
        "fastapi >= 0.78.0",
        "SQLAlchemy >= 1.4.37",
        "alembic >= 1.8.0",
    ],
    tests_require=[
        'pytest==7.1.1',
        'coveralls>=1.11.1',
    ],
    test_suite='runtests.runtests',
    include_package_data=True,
    python_requires='>=3.6',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],

    entry_points='''
        [console_scripts]
        fastmigrate=migrations.cli:db
    ''',
)