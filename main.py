# Main function.

import compile_db as cdb
import os.path as fpath
import argparse

def main(compileCommands: str):
    cdb.load_compile_commands(compileCommands)

def check_file(path, parser):
    if not fpath.isfile(path):
        parser.error('File {path} not found or invalid.')
    else:
        return path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='C/CPP static analyzer using clang-tidy.')
    parser.add_argument('input_file',
                        type=lambda file_path: check_file(file_path, parser),
                        help='Compile commands to load.')

    args = parser.parse_args()

    main(args.input_file)
