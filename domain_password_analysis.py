#!/usr/bin/env python
# USAGE
# MAKE SURE TO ADD HEADERS to the begining of your domain hash csv dump file: Domain,UserName,LMHash,NTHash

import pandas as pd

df = pd.read_csv(r'C:\Users\xkill\Documents\my_scripts\password_analysis\domain_hash_dump.csv')


# Filter out rows where Domain contains '$'
filtered_df = df[~(df['Domain'].str.contains('\$', na=False) | df['UserName'].str.contains('\$', na=False))]

# Find duplicates based on NTHash
duplicate_hashes = filtered_df[filtered_df.duplicated('NTHash', keep=False)]

# Sort by UserName
sorted_duplicates = duplicate_hashes.sort_values(by='NTHash')

lmhash_counts = df.groupby('LMHash').size().reset_index(name='Count')
lmhash_counts = lmhash_counts.sort_values('Count', ascending=False)


# Write sorted DataFrame to CSV
sorted_duplicates.to_csv('sorted_duplicates.csv', index=False)
print("DataFrame is written to sorted_duplicates CSV file successfully.")

# Write LMHash Count ANalysis DataFrame to CSV
lmhash_counts.to_csv('lmhash_counts.csv', index=False)
print("lmhash_counts is written to lmhash_counts CSV file successfully.")
