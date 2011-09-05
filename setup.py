# -*- coding: utf-8 -*-

from distutils.core import setup
import stonebear

setup(
        name =             'stonebear',
        version =          stonebear.__version__,
        description =      'Build and deployment tool for developing websites and web applications',
        long_description = open('README.rst').read(),
        author =           'chrisbuchholz',
        author_email =     'christoffer.buchholz@gmail.com',
        maintainer =       'chrisbuchholz',
        maintainer_email = 'christoffer.buchholz@gmail.com',
        license =          'GNU General Public License (GPL)',
        platforms =        ['MacOS', 'POSIX'],
        url =              'https://github.com/ChrisBuchholz/stonebear',
        packages =         ['stonebear'],
        package_data =     {},
        requires =         [],
        scripts =          ['bin/stonebear'],
        data_files =       [
            ('man/man1', ['man/man1/stonebear.1']),
            ('man/man2', ['man/man2/stonebear-config.2'])
        ],
        classifiers =      [
            'Environment :: Console',
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers'
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Natural Language :: English',
            'Operating System :: MacOS :: MacOS X'
            'Operating System :: POSIX',
            'Programming Language :: Python :: 2.7'
        ]
)
