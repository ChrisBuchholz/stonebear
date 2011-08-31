# this is an example config-file that uses all available options - to not use
# a config option, simply do not define it
#
# a stonebear config file must be call spiderd.py and be available in the
# directory that stonebear is called from
#
# a stonebeard.py config file is a simply python script containing a dictionary
# config[]
#
# this config requires third-party software:
#   jpegoptim
#   optipng
#   htmlcompressor
#   uglifyjs
#   yuicompressor

config = {
    # compilers; default=[]
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
            'yuicompressor -type css -o {file} {file}'
        ]
    ],

    # directories
    'input_dir':  'src',   # default
    'output_dir': 'build', # default

    # list of files to _not include in output_dir
    # default=[]
    'ignore': [
        '*.psd',
        '.DS_Store',
        '.*.swp',
        '*.pyc',
        'CACHE'
    ],

    # commands to run pre-build; default=""""""
    'prebuild': """
        echo 'command that executes before build process'
    """,

    # commands to run post-build; default=""""""
    'postbuild': """
        echo 'command that executes after build process'
    """

    # commands to run pre-push; default=""""""
    'prepush': """
        echo 'command that executes before push process'
    """,

    # commands to run post-push; default=""""""
    'postpush': """
        echo 'command that executes after push process'
    """

    # commands to run pre-clean; default=""""""
    'preclean': """
        echo 'command that executes before clean process'
    """,

    # commands to run post-clean; default=""""""
    'postclean': """
        echo 'command that executes after clean process'
    """

    # dictionary of environments
    # key is the name of the environment
    # value (multi-line string) is the push-command
    'envs': {
        'development': """
            rsync -az --delete build/ /var/www/
        """,
        'production': """
            rsync -az --delete build/ -e ssh user@host':/var/www/
        """
    }
}
