config = {
    'compilers': [
        [
            ['*.jpg', '*.jpeg'],
            'jpegoptim {file}'
        ],
        [
            ['*.png'],
            'optipng {file}'
        ],
        [
            ['*.html', '*.htm'],
            'htmlcompressor -o {file} {file}'
        ],
        [
            ['*.js'],
            'uglifyjs -o {file} {file}'
        ],
        [
            ['*.css'],
            'yuicompressor -o {file} {file}'
        ]
    ],

    'input':  ['src'],
    'output': ['build'],

    'remove_from_output_dirs': [
        '*.psd',
        '.*.swp',
        '.DS_Store'
    ],

    'postclean': """
        rm -rf development-build/ production-build/
    """,

    'environments': {
        'development': """
            rsync -azv --delete build/ development-build/
        """,
        'production': """
            rsync -azv --delete build/ production-build/
        """
    }
}
