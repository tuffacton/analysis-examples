import pandas as pd
import operator
import sys
import os
sys.path.insert(0,'../')

def txt_to_df(text_file_path):
    '''
    Takes a file path to a text file that follows the syntax of pipe-delimited values and converts it to a good dataframe.
    '''
    df = pd.read_csv(text_file_path, sep="|", header=None, low_memory=False)
    return df

def txt_to_pickle(text_file_path, filename):
    '''
    Takes a file path to a text file that follows the syntax of pipe-delimited values and converts it to a good dataframe.
    '''
    df = txt_to_df(text_file_path)
    df.to_pickle(filename)

def txt_to_column_df(data_file_path, clist_file_path):
    '''
    Takes a string file-path to a text file that follows the syntax of pipe-delimited values,
    and a string file-path to a list of their column names and converts it to a column-named dataframe
    for useful work!
    '''
    main_df = pd.read_csv(data_file_path, sep="|", header=None, low_memory=False)

    cHelp = open(clist_file_path, 'r')
    cHelpArray = []
    for line in cHelp:
        cHelpArray.append(line.rstrip())

    main_df.columns=cHelpArray
    return main_df
