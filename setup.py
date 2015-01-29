import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
readme = open('README.rst').read()

requirements = ['pyjwt>=0.3.1']
requirements_test = []

setup(
    name='django-openid-provider',
    version='0.1',
    packages=['openid_provider'],
    include_package_data=True,
    license='MIT License',
    description='A simple OpenID Connect Provider implementation for Djangonauts.',
    long_description=readme,
    url='http://github.com/juanifioren/django-openid-provider',
    author='Juan Ignacio Fiorentino',
    author_email='juanifioren@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=requirements
)