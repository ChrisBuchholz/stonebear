# -*- coding: utf-8 -*-

from distutils.core import setup
import stonebear

setup(
        name = "stonebear",
        version = stonebear.__version__,
        description = "",
        long_description = open('README.rst').read(),
        author = "chrisbuchholz",
        author_email = "christoffer.buchholz@gmail.com",
        license = "",
        platforms = [
            "MacOS",
            "POSIX"
        ],
        url = "https://github.com/ChrisBuchholz/stonebear",
        packages = ["stonebear"],
        package_data = {},
        requires = ["PyYAML (>=3.x)"],
        scripts = ["bin/stonebear"],
        data_files = [("man/man1", ["man/man1/stonebear.1"])],
        classifiers = [
            "Development Status :: 5 - Production/Stable",
            "Environment :: Console",
            "Intended Audience :: End Users/Desktop",
            "Intended Audience :: Developers",
            "Intended Audience :: System Administrators",
            "Natural Language :: English",
            "Operating System :: MacOS",
            "Operating System :: POSIX",
            "Programming Language :: Python",
            "Topic :: Utilities"
        ]
)
