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

def get_data_from_sql():
    query = '''
    SELECT customer_id, monthly_charges, tenure, total_charges
    FROM customers
    WHERE contract_type_id = 3;
    '''
    df = pd.read_sql(query, get_db_url('telco_churn'))
    return df







