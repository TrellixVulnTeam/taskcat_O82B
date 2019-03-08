from setuptools import setup
import datetime
import unittest
import os

with open('requirements.txt') as f:
    required = f.read().splitlines()

def test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests/unittest', pattern='test_*.py')
    return test_suite

setup(
    name='taskcat-v9',
    packages=['taskcat'],
    description='An OpenSource Cloudformation Deployment Framework',
    author='Tony Vattathil, Santiago Cardenas, Shivansh Singh, Jay McConnell, Andrew Glenn' ,
    author_email='tonynv@amazon.com, sancard@amazon.com, sshvans@amazon.com, jmmccon@amazon.com, andglenn@amazon.com',
    url='https://aws-quickstart.github.io/taskcat/',
    license='Apache License 2.0',
    download_url='https://github.com/aws-quickstart/taskcat/tarball/master',
    version = '0.9.0',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Testing',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X '
    ],
    scripts=[
        'bin/taskcat-v9'
    ],
    keywords=['aws', 'cloudformation', 'cloud', 'cloudformation testing', 'cloudformation deploy', 'taskcat'],
    install_requires=required,
    test_suite='setup.test_suite',
    include_package_data=True

)
