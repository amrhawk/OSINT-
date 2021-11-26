import os
import json
import csv
import pandas as pd

filter = "python red.py > output.json"
os.system(filter)

with open('output.json', encoding='utf-8-sig') as f_input:
    df = pd.read_json('output.json', lines=True)
    df.to_csv('reddit.csv', encoding='utf-8', index=False)
    print("Finished Downloading Reddit Data")