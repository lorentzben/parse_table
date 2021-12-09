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
    parsed_table = pd.DataFrame()
    num_chunks = int(len(tab)/100)
    num_v_chunk = int(len(tab.T)/3)
    for i in range(0,num_chunks):
        for j in range(0,num_v_chunk):
            current_chunk = tab.iloc[0+(i*100):100+(i*100), 0+(j*3):3+(j*3)]
            current_chunk.columns = ["datetime", "temp", "humid"]
            parsed_table = pd.concat([parsed_table, current_chunk], axis=0)
            parsed_table["temp2"] = parsed_table["temp"].str.extract(r'(\d+.\d+)').astype(float)
            parsed_table["humid2"] = parsed_table["humid"].str.extract(r'(\d+.\d+)').astype(float)
            p_table = parsed_table[["datetime", "temp2", "humid2"]]
            p_table.columns = ["datetime", "temp", "humid"]
    
    return p_table

def save_parsed_to_file(out,tab):
    tab.to_csv(out,index=False)

def main(arg):
    if arg.inital_dir:
        file_list = get_files_from_dir(arg.inital_dir)
        for fi in file_list:
            outname = fi[:-4]+"_parsed.csv"
            curr_tab = open_file_read_in_mem(fi)
            p_tab = parse_table_to_mem(curr_tab)
            save_parsed_to_file(outname,p_tab)
    if arg.infile:
        outname = arg.infile[:-4]+"_parsed.csv"
        table = open_file_read_in_mem(arg.infile)
        p_tab = parse_table_to_mem(table)
        save_parsed_to_file(outname,p_tab)
    


if __name__ == "__main__":
    # Build Argument Parser in order to facilitate ease of use for user
    parser = argparse.ArgumentParser(
        description="Handles the calling of the filter command for qiime because nextflow was messing with the string to call the command")
    parser.add_argument('-d', '--directory', action='store', required=False,
                        help="name of the directory holding TSV files to be parsed", dest='inital_dir')
    parser.add_argument('-f', '--file', action='store', required=False,
                        help="name of the TSV file to be parsed", dest='infile')
    args = parser.parse_args()
    main(args)
