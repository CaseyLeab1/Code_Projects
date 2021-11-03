import pandas as pd



def processandCleanseData(alldatadf):
  
    # Group by the user_id and path to find counts by path per user_id
    data_grouped = alldatadf.groupby(["user_id", "path"],as_index=False)["length"].sum()


    # convert outputdata using pivot table to create columns of Users and the distinct paths
    data_pivotdf = pd.pivot_table(data_grouped, values = 'length', index="user_id", columns = 'path').reset_index()
    outputdatadf = pd.DataFrame(data_pivotdf.to_records())
    
    return outputdatadf
 
    