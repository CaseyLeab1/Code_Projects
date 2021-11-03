
from repositories import file_repository as filerepo
from domain import data_stager, job_domain
from datetime import datetime





def main():
    start_datetime = datetime.now
    print ("Starting Data Cleanse Program: {0}", start_datetime)  
    
#find and read files to download
    alldataDF = filerepo.readCSVData()
    
#if any files read above process and cleanse the data   
    outputDF = data_stager.processandCleanseData(alldataDF)
    
 #output the cleansed data 
    job_domain.createOutputFile(outputDF)
    
    end_datetime = datetime.now
    print ("Data Cleanse Program Complete: {0}", end_datetime)  
    
if __name__ == '__main__':
    main()
