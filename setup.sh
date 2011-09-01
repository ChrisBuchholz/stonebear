#!/bin/bash

# requires:
#   ronn <https://github.com/rtomayko/ronn>
#   pandoc <http://johnmacfarlane.net/pandoc>

### generate manpages
echo "generate man pages"
VERSION=`python -c 'import stonebear; print stonebear.__version__'`
ronn man/man1/stonebear.1.ronn --style=toc --organization="stonebear ${VERSION}" --manual="stonebear manual"
ronn man/man2/stonebear-config.2.ronn --style=toc --organization="stonebear ${VERSION}" --manual="stonebear manual"

### convert README.md to HTML
echo "convert README.md to HTML; README.html"
pandoc -f markdown -t html README.md -o README.html

### convert README.md to reStructuredText
echo "convert README.md to reStructuredText; README.rst"
pandoc -f markdown -t rst README.md -o README.rst
