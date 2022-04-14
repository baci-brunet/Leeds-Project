import pandas as pd
import numpy as np
import re
import string


firms_df = pd.read_csv('/projects/sebr8260/Data/Diego/conames_clean.csv')
df = pd.read_csv('/projects/sebr8260/OutputRaw/FBC/FBC_2019_output.csv')

# lot = []
# for i in range(len(df.index)):
#     if df.loc[i, 'Matched Organizations'] != 'No Hits':
#         for firm_name in str(df.loc[i, 'Matched Organizations']).split(', '):
#             if firm_name != 'nan':
#                 key = '/'.join(firm_name.split('/')[1:2])
#                 lot.append((df.loc[i, 'URL'],
#                             df.loc[i, 'Title'],
#                             df.loc[i, 'Topics'],
#                             firm_name.split('/')[0], 
#                             firm_name.split('/')[1], 
#                             firm_name.split('/')[2]
#                            ))
#     else:
#         continue

# final_df = pd.DataFrame(lot, columns = ['URL', 'Title', 'Topics', 'Search Term', 'Time', 'Frequency'])
# final_df.to_csv('/projects/sebr8260/OutputRaw/Bloomberg/Bloomberg_2013_output.csv', index=False)


df['Permno'] = df['Search Term'].apply(lambda term: firms_df.loc[firms_df.loc[(firms_df['regexes'] == str(term)) | (firms_df['names.firms.1'] == str(term))].index[0], 'permno'])
df['Firm Name'] = df['Search Term'].apply(lambda term: firms_df.loc[firms_df.loc[(firms_df['regexes'] == str(term)) | (firms_df['names.firms.1'] ==str(term))].index[0], 'names.firms'])
df['Date'] = df['URL'].apply(lambda url: url.split('/')[2].split('_')[1])
df.to_csv('/projects/sebr8260/OutputRaw/FBC/FBC_2019_output.csv', index=False)
