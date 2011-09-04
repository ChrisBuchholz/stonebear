# -*- coding: utf-8 -*-

import os
import shutil
import fnmatch
import subprocess
from clean import clean

def match_files_to_filter(dir, files, filter, do):
    for fl in filter:
        for fn in fnmatch.filter(files, fl):
            do(dir + '/' + fn)

def walk_dir_n_do(dir, filter, do):
    for root, dirs, files in os.walk(dir):
        match_files_to_filter(root, files, filter, do)
        # walk_n_do dirs
        for dir in dirs:
            walk_dir_n_do(dir, filter, do)

def build(args, config):
    """
    clean and rebuild [output_dir] from [input_dir]
    """

    # run prebuild command
    subprocess.call(config['prebuild'], shell=True)

    cwd =    os.getcwd() + '/'
    input =  config['input']
    output = config['output']
    remove_from_output_dirs = config['remove_from_output_dirs']

    input_files =  []
    input_dirs =   []
    output_files = []
    output_dirs =  []
    rest_files =   []
    files =        []

    # find files and dirs
    for c, i in enumerate(input):
        if os.path.isdir(cwd + i):
            input_dirs.append(i)
            output_dirs.append(output[c])
        else:
            input_files.append(i)
            output_files.append(output[c])

    # directories
    for i, dir in enumerate(input_dirs):
        the_dir = dir
        if dir != output_dirs[i]:
            # input_dir to output_dir
            try:
                shutil.copytree(dir, output_dirs[i])
                the_dir = output_dirs[i]
            except OSError:
                raise
                sys.exit(1)
        # now we need to find all files that has matches on the ignore list and
        # remove those files from output_dir
        walk_dir_n_do(the_dir, remove_from_output_dirs, lambda f: os.remove(f))
        # compilers
        for compiler in config['compilers']:
            walk_dir_n_do(the_dir, compiler[0], lambda f:
                          subprocess.call(compiler[1].format(file=f),
                                          shell=True))

    # files
    for i, file in enumerate(input_files):
        if file != output_files[i]:
            try:
                shutil.copyfile(file, output_files[i])
                file = output_files[i]
            except OSError:
                raise
                sys.exit(1)
        files.append(file)

    # run compilers on rest_files
    for compiler in config['compilers']:
        match_files_to_filter(cwd, files, compiler[0], lambda f:
                              subprocess.call(compiler[1].format(file=f),
                                              shell=True))

    # run postbuild command
    subprocess.call(config['postbuild'], shell=True)
