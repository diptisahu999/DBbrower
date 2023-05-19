import os

directory = './dump/ABC_tbl/'
files = os.listdir(directory)

for file in files:
    if file.endswith('.json'):
        filepath = os.path.join(directory, file)
        os.system(f"mongoimport --db BMS_v2  --file {filepath}")



# mongodump --db ABC_tbl --out /home/div/download/mydb_backup
# mongodump --db ABC_tbl  --out /home/div/Download/ABC_tbl
# mongodump --db ABC_tbl --out BMS_v2.bson

