If you have a csv dump of a domain from NTDS.nit using secretsdump.py from impacket for instance. Simple open your csv and add the following to the first line:
```csv
Domain,UserName,LMHash,NTHash
```

Now change the line read_csv line in the code to the path of your password_hash.csv file. 

```sh
python3 domain_password_hash_analysis.py
```

Profit
