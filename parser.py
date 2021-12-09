#!/usr/bin/env python3

import pandas as pd
import numpy as np
import os
from os import path
import argparse
import subprocess
import glob


#print("hello world")

def get_files_from_dir(direct):
    targetPattern = direct+"/*.tsv"
    file_list = glob.glob(targetPattern)
    return file_list

def open_file_read_in_mem(file):
    table = pd.read_csv(file,sep="\t",header=None)
    return table

def parse_table_to_mem(tab):
    print("_parsed")

def save_parsed_to_file(tab):
    print("_saved")

def main(arg):
    if arg.inital_dir:
        file_list = get_files_from_dir(arg.inital_dir)
        for fi in file_list:
            curr_tab = open_file_read_in_mem(fi)
            print(curr_tab)
        print(file_list)
    if arg.infile:
        table = open_file_read_in_mem(arg.infile)
        print(table)
    if arg.outfile:
        print("Your outfile name is: " + arg.outfile)


if __name__ == "__main__":
    # Build Argument Parser in order to facilitate ease of use for user
    parser = argparse.ArgumentParser(
        description="Handles the calling of the filter command for qiime because nextflow was messing with the string to call the command")
    parser.add_argument('-d', '--directory', action='store', required=False,
                        help="name of the directory holding TSV files to be parsed", dest='inital_dir')
    parser.add_argument('-f', '--file', action='store', required=False,
                        help="name of the TSV file to be parsed", dest='infile')
    parser.add_argument('-o', '--outname', action='store', required=False,
                        help="name of the outfile, if no name is provided the original name will be appeneded", dest='outfile')
    args = parser.parse_args()
    main(args)
