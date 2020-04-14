# Throughout the exercises for Regression in Python lessons, you will use
# the following example scenario: As a customer analyst, I want to know
# who has spent the most money with us over their lifetime. I have monthly
# charges and tenure, so I think I will be able to use those two
# attributes as features to estimate total_charges. I need to do this
# within an average of $5.00 per customer.

import pandas as pd
import numpy as np
from env import host, user, password


# function to get url

def get_db_url(db_name):
    return f"mysql+pymysql://{user}:{password}@{host}/{db_name}"

# function that passes my query and my url to return df
def get_zillow_data_from_sql():
    query = '''
    SELECT
    bathroomcnt AS bathroom_count,
    bedroomcnt AS bedroom_count,
    calculatedfinishedsquarefeet AS square_feet,
    -- fips AS fips_number,
    -- ptype.propertylandusedesc,
    taxvaluedollarcnt AS home_value
    FROM properties_2017 AS prop
    JOIN
    predictions_2017 AS pred
    ON prop.parcelid = pred.parcelid
    JOIN
    propertylandusetype AS ptype
    ON prop.propertylandusetypeid = ptype.propertylandusetypeid

WHERE transactiondate
BETWEEN '2017-05-01' AND '2017-06-30' AND propertylandusedesc = 'Single Family Residential'

    '''
    df = pd.read_sql(query, get_db_url('zillow'))
    return df

# function to clean up my zillow dataframe
def prep_zillow(df):
    df = df.dropna()
    df['fips'] = df['fips'].astype(int)
    # df['propertylandusedesc'] = df['propertylandusedesc'].astype('category')
    df['square_feet'] = df['square_feet'].astype('int') # this is a string
    # df['propertylandusetypeid'] = df['propertylandusetypeid'].astype(int)
    return df

