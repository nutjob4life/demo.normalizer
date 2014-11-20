# encoding: utf-8

from setuptools import setup, find_packages
import os.path

setup(
    author='Sean Kelly',
    author_email='sean.kelly@jpl.nasa.gov',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    description='Demo Python package that depends on the ``plone.i18n`` package',
    entry_points={
        'console_scripts': ['normalize=demo.normalizer.main:main']
    },
    extras_require={},
    include_package_data=True,
    install_requires=[
        'setuptools',
        'plone.i18n'
    ],
    keywords=['demo', 'python', 'package', 'dependency', 'normalizer'],
    license='ALv2',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    maintainer='Sean Kelly',
    maintainer_email='sean.kelly@jpl.nasa.gov',
    name='demo.normalizer',
    namespace_packages=['demo'],
    packages=find_packages('src', exclude=['ez_setup', 'bootstrap']),
    package_dir={'': 'src'},
    url='http://github.com/nutjob4life/demo.normalizer',
    version='0.0.0',
    zip_safe=True
)
