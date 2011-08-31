# -*- coding: utf-8 -*-

import os
import shutil
import subprocess

def clean(args, config):
    """
    clean [output_dir]
    """

    # run preclean command
    subprocess.call(config['preclean'], shell=True)

    # clean output_dir
    output_dir = os.getcwd() + '/' + config['output_dir']
    try:
        if os.path.exists(output_dir):
            shutil.rmtree(output_dir)

        print "clean output_dir"
    except OSError as exc:
        if os.path.isdir(output_dir):
            print "could not modify %s" % output_dir
        else:
            raise
        sys.exit(1)

    # run postclean command
    subprocess.call(config['postclean'], shell=True)
