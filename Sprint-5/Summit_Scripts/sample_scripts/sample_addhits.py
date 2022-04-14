import pandas as pd
import numpy as np
import re
import string
import os
from os.path import exists

firms_df = pd.read_csv('/projects/sebr8260/Data/Diego/conames_clean.csv')
df = pd.read_csv('/projects/sebr8260/OutputRaw/Bloomberg/Bloomberg_2013_output.csv')

all_firms = []
for i in range(len(firms_df.index)):
    if firms_df.loc[i, 'done'] == 1:
        if isinstance(firms_df.loc[i, 'regexes'], str):
            all_firms.append(firms_df.loc[i, 'regexes'])
        else:
            all_firms.append(firms_df.loc[i, 'names.firms.1'])
                         
def add_hits(row, firm_list):
    loi = []
    for segment in str(row).split('[[TIME.START]]'):
        for firm in firm_list:
            if '*' in firm:
                search_term = r'\b{}'.format(firm.strip('*'))
            else:
                search_term = r'\b{}\b'.format(firm)
            if re.search(search_term.lower(), segment.lower()):
                loi.append((firm, segment.split('[[TIME.END]]')[0].strip(), len(re.findall(search_term.lower(), segment.lower()))))
    if not loi:
        return 'No Hits'
    else:
        return ', '.join(['{}/{}/{}'.format(tpl[0], tpl[1], tpl[2]) for tpl in loi])

df['Matched Organizations'] = df['RawText_preprocessed'].apply(lambda text: add_hits(text, all_firms))

df.to_csv('/projects/sebr8260/OutputRaw/Bloomberg/Bloomberg_2013_output.csv', index=False)
