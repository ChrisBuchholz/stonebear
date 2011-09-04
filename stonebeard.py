config = {
    'prebuild': """
        wget https://raw.github.com/ChrisBuchholz/stonebear/master/man/man1/stonebear.1.html -O man/man1/stonebear.1.html
        wget https://raw.github.com/ChrisBuchholz/stonebear/master/man/man2/stonebear-config.2.html -O man/man2/stonebear-config.2.html

        mkdir -p man man/man1 man/man2
    """
}
