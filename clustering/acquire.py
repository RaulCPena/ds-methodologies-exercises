import pandas as pd
from env import host, user, password

# function to get url

def get_db_url(db_name):
    return f"mysql+pymysql://{user}:{password}@{host}/{db_name}"

# pulls the data fron SQL and then

def get_zillow_data():
    query = '''
    SELECT * 
    FROM predictions_2017
    LEFT JOIN properties_2017 USING (parcelid)
    LEFT JOIN airconditioningtype USING (airconditioningtypeid)
    LEFT JOIN architecturalstyletype USING (architecturalstyletypeid)
    LEFT JOIN buildingclasstype USING (buildingclasstypeid)
    LEFT JOIN heatingorsystemtype USING (heatingorsystemtypeid)
    LEFT JOIN propertylandusetype USING (propertylandusetypeid)
    LEFT JOIN storytype USING (storytypeid)
    LEFT JOIN typeconstructiontype USING (typeconstructiontypeid)
    WHERE (latitude is not null) AND (longitude is not NULL)
    '''
    df = pd.read_sql(query, get_db_url('zillow'))
    
    df = df.sort_values(by = ['transactiondate'], axis = 0).drop_duplicates(keep = 'last', subset = 'parcelid')

    df.drop('id', axis = 1, inplace=True)

    return df

# a function that takes in a dataframe of observations and attributes and returns a dataframe where each row is an atttribute name, the first column is the number of rows with missing values for that attribute, and the second column is percent of total rows that have missing values for that attribute
def nulls_by_columns(df):
    total_missing = zillow.isnull().sum()
    avg_missing = missing / zillow.shape[0]
    missing_columns = pd.DataFrame({'num_rows_missing': total_missing, 'pct_rows_missing': avg_missing})
    return missing_columns