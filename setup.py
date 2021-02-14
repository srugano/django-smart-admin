# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os.path

here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
with open(readme_path, 'rb') as stream:
    readme = stream.read().decode('utf8')

setup(
    long_description=readme,
    long_description_content_type="text/x-rst",
    name='django-smart-admin',
    version='0.1.0',
    python_requires='==3.*,>=3.0.0,>=3.6',
    project_urls={"homepage": "https://github.com/saxix/django-smart-admin",
                  "repository": "https://github.com/saxix/django-smart-admin"
                  },
    author='sax',
    author_email='s.apostolico@gmail.com',
    keywords='django',
    packages=['smart_admin', 'smart_admin.templates', 'smart_admin.templates.templatetags'],
    package_dir={"": "src"},
    package_data={"smart_admin.templates": ["templates/admin/*.html"]},
    extras_require={
        'test': ['django-webtest',
                 'factory-boy',
                 'pytest',
                 'pyquery',
                 'pytest-echo',
                 'pytest-cov==2.*,>=2.11.1',
                 'pytest-django==4.*,>=4.1.0',
                 'pytest-pythonpath==0.*,>=0.7.3',
                 ]
    },
)