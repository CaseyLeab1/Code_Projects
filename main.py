from job_domain import createOutputFile
from data_stager import processandCleanseData
from file_repository import readCSVData
from datetime import datetime





def main():
    start_datetime = datetime.now
    print ("Starting Data Cleanse Program: {0}", start_datetime)  
    
#find and read files to download
    alldataDF = readCSVData()
    
#if any files read above process and cleanse the data   
    outputDF = processandCleanseData(alldataDF)
    
 #output the cleansed data 
    createOutputFile(outputDF)
    
    end_datetime = datetime.now
    print ("Data Cleanse Program Complete: {0}", end_datetime)  
    
if __name__ == '__main__':
    main()
