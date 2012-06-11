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

    'input': ['index.html', 'jquery-1.7.2.js', 'style.css'],
    'output': ['index_o.html', 'jquery-1.7.2_o.js', 'style_o.css']
}
