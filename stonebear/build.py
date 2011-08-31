# -*- coding: utf-8 -*-

import os
import shutil
import fnmatch
import subprocess
from clean import clean

def walk_n_do(dir, filter, do):
    for root, dirs, files in os.walk(dir):
        # remove matched files
        for fl in filter:
            for fn in fnmatch.filter(files, fl):
                do(root + "/" + fn)
        # walk_n_remove dirs
        for dir in dirs:
            walk_n_do(dir, filter, do)

def build(args, config):
    """
    clean and rebuild [output_dir] from [input_dir]
    """

    # run prebuild command
    subprocess.call(config['prebuild'], shell=True)

    # copy input_dir to output_dir and remove config[ignore] files from
    # output_dir

    # set input_dir and output_dir
    input_dir = os.getcwd() + '/' + config['input_dir']
    output_dir = os.getcwd() + '/' + config['output_dir']

    # remove output_dir first, and then copy output_dir to the path of
    # input_dir
    clean(args, config)

    # and then copy input_dir to output_dir
    try:
        shutil.copytree(input_dir, output_dir)
        print "copy input_dir to output_dir"
    except OSError as exc:
        if not os.path.isdir(input_dir):
            print "%s is not a directory" % input_dir
        elif not os.path.isdir(output_dir):
            print "%s is not a directory" % output_dir
        else:
            raise
        sys.exit(1)

    # now we need to find all files that has matches on the ignore list and
    # remove those files from output_dir
    walk_n_do(output_dir, config['ignore'], lambda f: os.remove(f))
    print "remove matched (ignore) files"

    # compilers
    for compiler in config['compilers']:
        walk_n_do(output_dir, compiler[0], lambda f:
                       subprocess.call(compiler[1].format(file=f), shell=True))

    # run postbuild command
    subprocess.call(config['postbuild'], shell=True)
