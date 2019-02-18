"""Vrisovanje."""
import os
import setuptools

# Get the long description from README.
with open('README.rst', 'r') as fh:
    long_description = fh.read()

# Get package metadata from '__about__.py' file.
about = {}
base_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(base_dir, 'vrisovanje', '__about__.py'), 'r') as fh:
    exec(fh.read(), about)

setuptools.setup(
    name=about['__title__'],
    use_scm_version=True,
    description=about['__summary__'],
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author=about['__author__'],
    author_email=about['__email__'],
    url=about['__url__'],
    license=about['__license__'],
    # Exclude tests from built/installed package.
    packages=setuptools.find_packages(),
    python_requires='>=3.6, <3.7',
    install_requires=[
        'Sphinx~=1.8.4',
        'sphinx_rtd_theme~=0.4.3',
    ],
    keywords='scout tabornik vrisovanje',
)
