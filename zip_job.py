import string
import sys
import os
import zipfile
import logging

abc_array=list(string.ascii_lowercase)

version = os.environ.get("VERSION")

for letter in abc_array:
   try: 
       with open(f'/tmp/{letter}.txt','w') as file:
           pass
   except Exception as ex:
       print(f"Failed to create {letter}.txt: {ex}")
       sys.exit(1)



for letter in abc_array:
    try:
        with zipfile.ZipFile(f'/tmp/{letter}_{version}.zip', 'w') as zip_file:
            zip_file.write(f'/tmp/{letter}.txt')
    except Exception as ex:
        print(f"Failed to create {letter}.zip: {ex}")
        sys.exit(1)



