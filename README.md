If you have a dump of a domain or multiple domains from NTDS.nit using secretsdump.py from impacket for instance. You can combine them by copy and pasting the output to Excel, then use Excel's Data>Text to Columns > set the delimiter to a full colon, and press enter to completion.

Save the file as a csv.

Open your csv and add the following to the first line:
```csv
Domain,UserName,LMHash,NTHash
```

Now change the line read_csv line in the code to the path of your password_hash.csv file. 

```sh
python3 domain_password_hash_analysis.py
```

Output will be 2 csv files...one showing accounts using same passwords paired up close...then a second csv with a count of hash, the hash, and the associated accounts all using the same password.

$Profit$
