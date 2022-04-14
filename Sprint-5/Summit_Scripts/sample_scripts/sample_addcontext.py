import pandas as pd
import numpy as np
import collections
import os
import re
import time

tv_df = pd.read_csv('/projects/sebr8260/Data/CorporaData/2013/CNBC.Text.2013.1.csv')
output_df = pd.read_csv('/projects/sebr8260/OutputRaw/CNBC/CNBC_2013_output.csv')
output_path = '/projects/sebr8260/OutputRaw/CNBC/CNBC_2013_output.csv'

tv_df.columns = ['URL', 'Title', 'RawText']
tv_df['RawText_preprocessed'] = tv_df['RawText'].apply(lambda text: str(text).split('TOPICS: TOPIC FREQUENCY ')[0])
tv_df['RawText_preprocessed'] = tv_df['RawText_preprocessed'].apply(lambda text: str(text)[str(text).find('[[TITLE.END]] ') + len('[[TITLE.END]] '):])       
del tv_df['RawText']

def add_context_window(tv_corpora, output):
    output['Context Window'] = None
    for i in range(len(output.index)):
        context = []
        list_of_indices = []
        firm = str(output.loc[i, 'Search Term'])
        raw_text = tv_corpora.loc[tv_corpora['Title'] == output.loc[i, 'Title']].index[0]
        for segment in tv_corpora.loc[raw_text, 'RawText_preprocessed'].split('[[TIME.START]]'):
            if output.loc[i, 'Time'] == segment.split('[[TIME.END]]')[0].strip():
                list_of_indices
                if '*' in firm:
                    search_term = r'\b{}'.format(firm.strip('*'))
                else:
                    search_term = r'\b{}\b'.format(firm)
                if int(output.loc[i, 'Frequency']) > 1:
                    list_of_indices = [m.start() for m in re.finditer(search_term.lower(), segment.lower())]
                    for ind in list_of_indices:
                        context_sentence = segment[ind-25:ind + len(firm) + 200]
                        context.append(context_sentence)
                    output.loc[i, 'Context Window'] = '||'.join(context)
                else:
                    firm_ind = re.search(search_term.lower(), segment.lower()).start()
                    output.loc[i, 'Context Window'] = segment[firm_ind-35:firm_ind + len(firm) + 200]

                
            else:
                continue
    return output

final = add_context_window(tv_df, output_df)
final.to_csv(output_path, index=False)


