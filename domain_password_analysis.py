import pandas as pd


df = pd.read_csv(r'C:\Users\xkill\path\to\password_dump.csv')
# password_dump must have metadata of Domain, UserName, LMHash, NTHash

# Filter out rows where Domain contains '$'
#filtered_df = df[(~df['Domain'].str.contains('\$'))or(~df['UserName'].str.contains('$'))]
filtered_df = df[~(df['Domain'].str.contains('\$', na=False) | df['UserName'].str.contains('\$', na=False))]

# Find duplicates based on NTHash
duplicate_hashes = filtered_df[filtered_df.duplicated('NTHash', keep=False)]
# Sort by UserName
sorted_duplicates = duplicate_hashes.sort_values(by='NTHash')
print(sorted_duplicates)

# Write sorted DataFrame to CSV
sorted_duplicates.to_csv('sorted_duplicates.csv', index=False)
print("DataFrame is written to sorted_duplicates CSV file successfully.")


# Group by 'NTHash' and aggregate
result = df.groupby('NTHash').agg({
    'NTHash': 'size',  # Count the occurrences of each hash
    'UserName': lambda x: ', '.join(x.dropna().astype(str))  # Concatenate the user names, handling NaN values
}).rename(columns={'NTHash': 'Count', 'UserName': 'AccountsWithPassword'})
sort_results=result.sort_values('Count', ascending=False)

# Write NTHash Count ANalysis DataFrame to CSV
sort_results.to_csv('NTHash_counts.csv', index=True)
print("lmhash_counts is written to lmhash_counts CSV file successfully.")
