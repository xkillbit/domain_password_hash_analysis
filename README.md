If you have a dump of a domain from NTDS.nit using secretsdump.py from impacket for instance. 

Copy and paste the output to Excel, then use Excel's Data>Text to Columns > set the delimiter to a full colon, and press enter to completion.

Save the file as a csv.

Open your csv and add the following to the first line:
```csv
Domain,UserName,LMHash,NTHash
```

Now change the line read_csv line in the code to the path of your password_hash.csv file. 

```sh
python3 domain_password_hash_analysis.py
```

Profit
