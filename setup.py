import imp
import os
from setuptools import setup, find_packages

version = imp.load_source(
    'mlflow.version', os.path.join('mlflow', 'version.py')).VERSION


# Get a list of all files in the JS directory to include in our module
def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


# Prints out a set of paths (relative to the mlflow/ directory) of files in mlflow/server/js/build
# to include in the wheel, e.g. "../mlflow/server/js/build/index.html"
js_files = package_files('mlflow/server/js/build')

setup(
    name='mlflow',
    version=version,
    packages=find_packages(exclude=['tests', 'tests.*']),
    package_data={"mlflow": js_files},
    install_requires=[
        'awscli',
        'click>=6.7',
        'databricks-cli',
        'requests>=2.17.3',
        'six>=1.10.0',
        'uuid',
        'gitpython',
        'gunicorn',
        'Flask',
        'numpy',
        'pandas',
        'scipy',
        'scikit-learn',
        'python-dateutil',
        'protobuf',
        'gitpython',
        'pyyaml',
        'boto3',
        'querystring_parser',
    ],
    entry_points='''
        [console_scripts]
        mlflow=mlflow.cli:cli
    ''',
    zip_safe=False,
    author='Databricks',
    description='MLflow: An ML Workflow Tool',
    long_description=open('README.rst').read(),
    license='Apache License 2.0',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='ml ai databricks',
    url='https://mlflow.org/'
)
