import ast
import io
import re

from setuptools import setup, find_packages

with io.open('README.md', 'rt', encoding="utf8") as f:
    readme = f.read()

_description_re = re.compile(r'description\s+=\s+(?P<description>.*)')

with open('lektor_google_search.py', 'rb') as f:
    description = str(ast.literal_eval(_description_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    author='Lissan Zahid',
    author_email='lissane2013@gmail.com',
    description=description,
    keywords='Lektor plugin',
    license='MIT',
    long_description=readme,
    long_description_content_type='text/markdown',
    name='lektor-google-search',
    packages=find_packages(),
    py_modules=['lektor_google_search'],
    url='https://github.com/eldjoko/lektor-google-search',
    version='0.1',
    classifiers=[
        'Framework :: Lektor',
        'Environment :: Web Environment',
        'Environment :: Plugins',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'lektor.plugins': [
            'google-search = lektor_google_search:GoogleSearchPlugin',
        ]
    }
)
