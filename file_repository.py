
import pandas as pd
import string
import os
from dotenv import load_dotenv
load_dotenv()

def readCSVData():
       
    source_url_base =  os.getenv("AWS_S3_URL")
    file_names = list(string.ascii_lowercase)

    # Create empty dataframe with column  names
    column_names  = os.getenv("File_Column_Names").split(",")
    alldataDF = pd.DataFrame(column_names)
    
    # loop thru the files at the URL and append to the alldataDF dataframe
    for file in file_names:

        url = source_url_base + file +".csv"
        print("processing file: {0}",url)        
        alldataDF = alldataDF.append(pd.read_csv(url))

    return alldataDF

    