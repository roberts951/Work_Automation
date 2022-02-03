# Python program to convert
# JSON file to CSV
  
import json
import csv
import pandas as pd
from datetime import date

today = str(date.today())

jsfile = input("Full path to .json file:")
output_csv = (today+"_Sentinel_Rules2Csv.csv")

print("Converting json to csv...")

with open(jsfile,'r') as f:
    data = json.loads(f.read())
    
# Flatten data
df_nested_list = pd.json_normalize(data,'resources',['properties','displayName'],errors='ignore')
df_nested_list.to_csv(output_csv)

kept_columns=["","kind","properties.displayName","properties.description","properties.severity","properties.enabled","properties.incidentConfiguration.createIncident"]

data = pd.read_csv(output_csv)
for col in data.columns:
    if col in kept_columns:
        continue
    else:
        data.drop(
            labels=col,
            axis=1,
            inplace=True
    )

data.to_csv(output_csv)

print("File saved as",output_csv,"(next to this script)")