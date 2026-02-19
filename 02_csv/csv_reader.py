import csv
import os



def load_csv(filename:str):
    #Workaround für Umgang mit relativen Pfaden
    script_dir = os.path.dirname(__file__)
    full_path= os.path.join(script_dir,filename)
    users=[]

    with open(full_path,newline='',encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
           # print(row['name'], row['email'])
           users.append((row['name'], row['email']))
    return users