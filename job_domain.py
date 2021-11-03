
from numpy.core.arrayprint import DatetimeFormat
import pandas as pd
import datetime



def createOutputFile(outputDF):
    
    outputfilename="PathViewByUserIDOutput_" +  datetime.datetime.now().strftime('%Y%m%d%H%M%S')  +"_.csv"  
    outputDF.to_csv(outputfilename,index=False)