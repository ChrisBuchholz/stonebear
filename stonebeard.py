config = {
    'input':    ['stonebear.1.html', 'stonebear-config.2.html'],
    'output':   ['man/man1/stonebear.1.html',
                 'man/man2/stonebear-config.2.html'],
    'prebuild': """
        wget https://raw.github.com/ChrisBuchholz/stonebear/master/man/man1/stonebear.1.html
        wget https://raw.github.com/ChrisBuchholz/stonebear/master/man/man2/stonebear-config.2.html
    """,
    'postbuild': """
        rm stonebear.1.html stonebear-config.2.html
    """,
    'postclean': """
        rm -rf man/
    """
}
