'''
This script searches in csv files for duplicates, and if it finds some, it highlights them in a
separate column and mentions, where it found it.

Format for the input files:
    ref;title
    acm;Paper for showing things
    ieee;Research of some important stuff
'''
import numpy as np
import pandas as pd

from utils import utils
from langdetect import detect
from tkinter import filedialog as fd
from utils import config



data_folder, files = utils.get_files_with_type_from_folder('.csv')

df = pd.concat([pd.read_csv(f, sep=";") for f in files]).reset_index(drop=True)

for columns in df.columns:
    df['title_low'] = df['title'].str.lower()

# since the duplicated function of pandas is case-sensitive, we lowercase the titles
df['duplicated'] = np.where(df['title_low'].duplicated(), True, '')

#  Select all files where duplicated is True
df_duplicates = df.loc[df['duplicated'] == 'True']

df['language'] = df['title'].apply(detect)

# Yes I know. Never iterate over pandas arrays. If you know better, please fix.
for index, row in df_duplicates.iterrows():
    # get the index of the row, where title of the current duplicate first appears in df
    idx = (df['title_low'] == row['title_low']).idxmax()
    # get the ref of this
    ref = df.iloc[idx]['ref']
    df.loc[df.index[index], 'origin'] = ref


df.to_csv("output.csv", index=False, sep=";", encoding='utf8')