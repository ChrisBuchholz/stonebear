config = {
    'compilers': [
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

    'input': ['index.html', 'script.js', 'style.css'],
    'output': ['index_o.html', 'script_o.js', 'style_o.css']
}
