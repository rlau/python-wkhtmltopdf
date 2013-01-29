from setuptools import setup, find_packages

setup(
    name='wkhtmltopdf',
    version='master',
    description='Simple python wrapper for wkhtmltoimage and wkhtmltopdf',
    long_description = "%s\n\n%s" % (open('README.rst', 'r').read(), open('AUTHORS.rst', 'r').read()),
    author='rlau',
    author_email='ryan.m.lau at gmail.com',
    license='BSD',
    url='http://github.com/rlau/python-wkhtmltoimage',
    packages = find_packages(),
    dependency_links = [],
    install_requires = [],
    include_package_data=True,
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
