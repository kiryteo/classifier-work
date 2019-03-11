import pandas as pd

df = pd.read_csv('TGSSADR1_7sigma_catalog.tsv', sep='\t')

#print(df.keys())

#print(df['RA'])
#print(df['DEC'])

df_new = df[['Source_name', 'RA', 'DEC']]
print(df_new)