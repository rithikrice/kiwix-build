#!/usr/bin/env python3

# import os, sys, shutil
# import argparse
# import ssl
# import urllib.request
# import subprocess
# import platform
# from collections import OrderedDict
#
# from dependency import Dependency
# from dependency_utils import ReleaseDownload, Builder, GitClone
# from utils import (
#     pj,
#     remove_duplicates,
#     add_execution_right,
#     get_sha256,
#     print_progress,
#     setup_print_progress,
#     download_remote,
#     StopBuild,
#     SkipCommand,
#     Defaultdict,
#     Remotefile,
#     Context)

import os
import sys
import argparse

from builder import Builder
from target import target_platforms


# REMOTE_PREFIX = 'http://download.kiwix.org/dev/'
#
# SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
#
#

# def which(name):
#     command = "which {}".format(name)
#     output = subprocess.check_output(command, shell=True)
#     return output[:-1].decode()

def parse_args():
    parser = argparse.ArgumentParser()
    # parser.add_argument('targets', default='kiwix-tools', nargs='?', metavar='TARGET', choices=Dependency.all_deps.keys())
    parser.add_argument('targets', default='kiwix-tools', nargs='?', metavar='TARGET')
    parser.add_argument('--working-dir', default='.')
    parser.add_argument('--lib-prefix', default=None)
    parser.add_argument('--target-platform', default='native_dyn', choices=target_platforms)
    parser.add_argument('--verbose', '-v', action='store_true',
                        help="Print all logs on stdout instead of in specific log files per commands")
    parser.add_argument('--hide-progress', action='store_false', dest='show_progress',
                        help="Hide intermediate progress information.")
    parser.add_argument('--skip-source-prepare', action='store_true',
                        help="Skip the source download part")
    parser.add_argument('--build-deps-only', action='store_true',
                        help="Build only the dependency of the specified targets.")

    subgroup = parser.add_argument_group('advanced')
    subgroup.add_argument('--no-cert-check', action='store_true',
                          help="Skip SSL certificate verification during download")
    subgroup.add_argument('--clean-at-end', action='store_true',
                          help="Clean all intermediate files after the (successful) build")

    subgroup = parser.add_argument_group('custom app', description="Android custom app specific options")
    subgroup.add_argument('--android-custom-app', help="The custom android app to build")
    subgroup.add_argument('--zim-file-url', help="The url of the zim file to download")
    subgroup.add_argument('--zim-file-size', help="The size of the zim file.")

    args = parser.parse_args()

    if args.targets == 'kiwix-android-custom':
        error = False
        if not args.android_custom_app:
            print("You need to specify ANDROID_CUSTOM_APP if you "
                  "want to build a kiwix-android-custom target")
            error = True
        if not args.zim_file_url and not args.zim_file_size:
            print("You need to specify ZIM_FILE_SIZE or ZIM_FILE_URL if you "
                  "want to build a kiwix-android-custom target")
            error = True
        if error:
            sys.exit(1)
    return args


if __name__ == "__main__":
    options = parse_args()
    options.working_dir = os.path.abspath(options.working_dir)
    # print(options)
    # setup_print_progress(options.show_progress)
    builder = Builder(options)
    builder.run()
