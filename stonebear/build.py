# -*- coding: utf-8 -*-

import os
import shutil
import fnmatch
import subprocess
from clean import clean

def match_files_to_filter(dir, files, filter, do):
    """
    pass all files in dir that matches filter to do
    """
    for fl in filter:
        for fn in fnmatch.filter(files, fl):
            do(dir + '/' + fn)

def walk_dir_n_do(dir, filter, do):
    for root, dirs, files in os.walk(dir):
        match_files_to_filter(root, files, filter, do)
        # walk_n_do dirs
        for dir in dirs:
            walk_dir_n_do(dir, filter, do)

def create_preceding_dirs(dir_str):
    """
    parse dir_str to see if it represents a dir or file, or a tree
    if it represents a tree, it will make sure that any preceding directories
    exists for the final distination of dir_str
    """
    tree = []
    cwd = os.getcwd() + '/'

    for t in dir_str.split('/'):
        if t:
            tree.append(t)

    del tree[-1]

    for t in tree:
        if not os.path.exists(cwd + t):
            os.mkdir(cwd + t)

def copy_tree(inputdir, outputdir):
    """
    wrapper function for shutil.copytree that enables overwrite of output
    directory
    """
    # remove outputdir if it already exists
    if os.path.exists(outputdir):
        try:
            shutil.rmtree(outputdir)
        except OSError:
            raise
            sys.exit(1)
    # copy inputdir to outputdir
    try:
        shutil.copytree(inputdir, outputdir)
        return outputdir
    except OSError:
        raise
        sys.exit(1)

def copy_file(inputfile, outputfile):
    """
    wrapper function for shutil.copyfile that enables overwrite of output file
    """
    # remove outputfile if it already exists
    if os.path.exists(outputfile):
        try:
            os.remove(outputfile)
        except OSError:
            raise
            sys.exit(1)
    # copy inputfile to outputfile
    try:
        shutil.copyfile(inputfile, outputfile)
        return outputfile
    except OSError:
        raise
        sys.exit(1)

def build(args, config):
    """
    build process
    will run [prebuild] commands, copy [input] to [output], remove files matching
    [remove_from_output_dirs] from directories in [output], run compilers on
    matching files in [output] and then run [postbuild] commands
    dirs in [output]
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
            copy_tree(dir, output_dirs[i])
            dir = output_dirs[i]
        # now we need to find all files that has matches on the ignore list and
        # remove those files from output_dir
        walk_dir_n_do(dir, remove_from_output_dirs, lambda f: os.remove(f))
        # compilers
        for compiler in config['compilers']:
            walk_dir_n_do(dir, compiler[0], lambda f:
                          subprocess.call(compiler[1].format(file=f),
                                          shell=True))

    # files
    for i, file in enumerate(input_files):
        if file != output_files[i]:
            copy_file(file, output_files[i])
            file = output_files[i]
        files.append(file)

    # run compilers on rest_files
    for compiler in config['compilers']:
        match_files_to_filter(cwd, files, compiler[0], lambda f:
                              subprocess.call(compiler[1].format(file=f),
                                              shell=True))

    # run postbuild command
    subprocess.call(config['postbuild'], shell=True)
